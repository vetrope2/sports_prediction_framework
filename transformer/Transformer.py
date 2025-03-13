from datawrapper.DataWrapper import DataWrapper
from transformer.BaseTransformer import BaseTransformer

class Transformer:
    transformations = {'names_to_ids':False, 'names_to_ids_scope':False, 'remove_small_seasons':False,
              'result_column':False, 'score_diff':False, 'round_column':False, 'date_from_time':False,
              'only_latest_odds': False, 'only_first_odds': False, 'first_and_latest_odds': False}

    base_transformer = BaseTransformer()



    def load_from_dict(self,transform_dict: dict):
        for key, value in transform_dict.keys(), transform_dict.values():
            if key in self.transformations.keys():
                self.transformations[key] = value
            else:
                print("Invalid param")

    def load_from_list(self, transform_list: list):
        for elem in transform_list:
            if elem in self.transformations.keys():
                self.transformations[elem] = True


    def transform(self, wrapper: DataWrapper):
        if self.transformations['only_first_odds']:
            wrapper = self.base_transformer.get_first_odds(wrapper)
        if self.transformations['only_latest_odds']:
            wrapper = self.base_transformer.get_latest_odds(wrapper)
        if self.transformations['first_and_latest_odds']:
            wrapper = self.base_transformer.get_first_and_latest_odds(wrapper)

        return wrapper