# **Image Classification for MNIST Dataset with Variational Autoencoder (VAE)**

This project involves an implementation of a Variational Autoencoder (VAE) to generate hand-written images from the MNIST dataset and save a grid of 15 x 15 digits as a vae\_image.png file.

**Packages Used**

- Keras
- Tensorflow
- Numpy
- Matplotlib

**How the VAE Model Works**

**Encoder Network**

The encoder network takes an image as input and outputs the mean and variance of the latent distribution.

**Decoder Network**

The decoder network takes a sample from the latent distribution as input and generates an image.

**Loss Function**

The parameters of a VAE are trained via two loss functions: a reconstruction loss which forces the decoded samples to match the initial inputs, and a regularization loss which helps to learn well-formed latent spaces while reducing overfitting to the trained data. But because the dual loss of a VAE does not fit the sample-wise function of the form loss (input, target), a custom layer is used to compute the VAE loss.

**Results**

The 15 x 15 grid of hand-written sample digit images will be produced by the trained VAE and will be saved as a vae\_image.file.

**License**

This project is licensed under the MIT license.
