# AutoCraft
A Deep Neural Network for generating StarCraft II commentary, based on pytorch.

1. We first train an LSTM Encoder-Transformer Decoder architecture using a video captioning framework, where a single video can have multiple correct captions and the model learns to generate sentences based on the seen video-caption training data.
2. We proceed to translate the generated captions by training a text to speech autoencoder on voice spectograms.
