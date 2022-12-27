#Used for preparing data for testing the trained model for predictions.

from transformers import BertTokenizer
import tensorflow as tf


class DataPreprocess():

    def __init__(self):

        self.tokenizer= BertTokenizer.from_pretrained('bert-base-cased')

    def prepare_data(self,input_text):
        tokenized_text = self.tokenizer.encode_plus(
            input_text,
            max_length=256,
            truncation=True,
            padding='max_length',
            add_special_tokens=True,
            return_tensors='tf'
        )

        return {
            'input_ids': tf.cast(tokenized_text.input_ids, tf.float64),
            'attention_mask': tf.cast(tokenized_text.attention_mask, tf.float64)
        }