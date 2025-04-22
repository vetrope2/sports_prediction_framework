import torch
from torch import Tensor
from torch.nn import Embedding, ModuleList, LogSoftmax, Dropout
from typing import Optional, Tuple
import pandas as pd

from datawrapper.sport.MatchWrapper import MatchWrapper
from model.torch.TorchModule import TorchModule



class TorchFlat(TorchModule):
    """
    A simple feedforward network that takes team embeddings (home and away),
    concatenates them, and passes through multiple dense layers to predict match outcomes.
    """

    def __init__(self, pretrained_weights: Optional[Tensor] = None) -> None:
        """
        Initializes the model, optionally using pretrained embeddings.

        :param pretrained_weights: Optional pretrained weights for team embeddings
        """
        super(TorchFlat, self).__init__()
        if pretrained_weights is not None:
            self.embedding: Embedding = Embedding.from_pretrained(pretrained_weights)
        else:
            self.embedding: Optional[Embedding] = None

    def complex_init(self) -> None:
        """
        Initializes the dense architecture of the model according to the specified type.
        """
        if self.architecture_type == 'rectangle':
            self.dense_dims = [self.dense_dim] * (self.n_dense - 2)
        elif self.architecture_type == 'pyramid':
            step = int((self.dense_dims + self.out_dim) / self.n_dense)
            dim = self.dense_dims
            for _ in range(self.n_dense - 1):
                self.dense_dims.append(dim)
                dim = dim - step

        lin_layers = []
        lin_layers.append(torch.nn.Linear(self.embed_dim * 2, self.dense_dims[0]))
        for i in range(self.n_dense - 2):
            lin_layers.append(torch.nn.Linear(self.dense_dims[i], self.dense_dims[i + 1]))
        lin_layers.append(torch.nn.Linear(self.dense_dims[self.n_dense - 2], self.out_dim))

        self.lin_layers: ModuleList = ModuleList(lin_layers)
        self.out: LogSoftmax = LogSoftmax(dim=1)
        self.drop: Dropout = Dropout(p=0.1)

    def forward(self, data: pd.DataFrame, team_home: Tensor, team_away: Tensor) -> Tensor:
        """
        Defines the forward pass of the model.

        :param data: Input data (not used directly here)
        :param team_home: Tensor of home team IDs
        :param team_away: Tensor of away team IDs
        :return: Log-probabilities tensor with shape [batch_size, out_dim]
        """
        home_emb = self.embedding(team_home)
        away_emb = self.embedding(team_away)
        x = torch.cat((home_emb, away_emb), 1)

        for layer in self.lin_layers:
            x = self.activation(layer(x))
            x = self.drop(x)

        x = self.out(x)
        return x.reshape(-1, self.out_dim)

    def set_parameters_from_wrapper(self, wrapper: MatchWrapper) -> None:
        """
        Initializes the embedding layer based on the dataset's metadata.

        :param wrapper: A MatchWrapper instance containing team count info
        """
        if self.embedding is None:
            self.embedding = Embedding(wrapper.total_number_of_teams, self.embed_dim)

    def get_features_batch(self, features: pd.DataFrame, batch_index: int) -> Tuple[pd.DataFrame, Tensor, Tensor]:
        """
        Retrieves a batch of home and away team IDs from the dataset.

        :param features: The full features DataFrame
        :param batch_index: Starting index of the batch
        :return: A tuple (features_df, home_team_tensor, away_team_tensor)
        """
        home = torch.from_numpy(
            features.iloc[batch_index:batch_index + self.batch_size]['HID'].values.astype('int64'))
        away = torch.from_numpy(
            features.iloc[batch_index:batch_index + self.batch_size]['AID'].values.astype('int64'))
        return features, home, away

    def get_labels_batch(self, labels: pd.DataFrame, batch_index: int) -> Tensor:
        """
        Retrieves a batch of match results as a tensor.

        :param labels: The full labels DataFrame
        :param batch_index: Starting index of the batch
        :return: A tensor of labels for the batch
        """
        result = torch.from_numpy(
            labels.iloc[batch_index:batch_index + self.batch_size].values.astype('int64').reshape(-1,))
        return result