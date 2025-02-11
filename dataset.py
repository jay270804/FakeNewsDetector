
import torch
from torch.utils.data import Dataset
from title_tokenizer import train_df, test_df, train_title_encodings, test_title_encodings

class NewsDataset(Dataset):
    """
    A PyTorch dataset class for news data.


    Attributes:
        encodings (dict): A dictionary of feature encodings.
        labels (list): A list of corresponding labels.
    """

    def __init__(self, encodings: dict, labels: list):
        """
        Initializes the NewsDataset instance.


        Args:
            encodings (dict): A dictionary of feature encodings.
            labels (list): A list of corresponding labels.
        """
        self.encodings = encodings
        self.labels = labels

    def __len__(self) -> int:
        """
        Returns the number of samples in the dataset.

        Returns:
            int: The number of samples in the dataset.
        """
        return len(self.labels)

    def __getitem__(self, index: int) -> dict:
        """
        Retrieves a data sample from the dataset at the specified index.


        Args:
            index (int): The index of the sample to retrieve.

        Returns:
            dict: A dictionary containing the feature encodings and corresponding label.
        """
        # Explain why we use this approach instead of direct indexing
        item = {key:value[index] for key, value in self.encodings.items()}
        item['label'] = torch.tensor(self.labels[index])
        return item

# Create instances of NewsDataset for training and testing data
train_dataset = NewsDataset(train_title_encodings, train_df['label'].tolist())
test_dataset = NewsDataset(test_title_encodings, test_df['label'].tolist())
