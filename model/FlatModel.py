from model.NeuralModel import NeuralModel
from torch_model.TorchFlat import TorchFlat
from datawrapper.sport.MatchWrapper import MatchWrapper
import torch

from typing import Optional


class FlatModel(NeuralModel):

    def __init__(self, pretrained_weights: Optional[torch.Tensor] = None, **kwargs) -> None:
        """
        Initialize the FlatModel. Creates an instance of the TorchFlat model and sets it up.

        Args:
            pretrained_weights (Optional[torch.Tensor]): Weights to initialize the model with,
                                                          if provided. Defaults to None.
            **kwargs: Additional keyword arguments passed to the parent class initializer.
        """
        # Initialize the TorchFlat model with optional pretrained weights
        super().__init__(**kwargs)
        self.model = TorchFlat(pretrained_weights)

        # Call the complex initialization of the model to set up the layers
        self.model.complex_init()

    def set_parameters_from_wrapper(self, wrapper: MatchWrapper) -> None:
        """
        Adjust the model parameters based on the provided MatchWrapper.

        Args:
            wrapper (MatchWrapper): The wrapper that contains match-related data used to
                                     configure the model (e.g., number of teams).
        """
        # Set model parameters using data from the wrapper (e.g., number of teams)
        self.model.set_parameters_from_wrapper(wrapper)