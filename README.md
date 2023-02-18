# vision5
Wavelet
5.1. Pyramid
5.1.1. For the “Mona Lisa” image, build a 5 level Gaussian pyramid and display it in a format. Also, implement and
display a Laplacian (difference of Gaussian (DoG)) pyramid.
5.1.2. Describe how separability and cascading can help to speed up Gaussian smoothing and design a fast algorithm
for computing a 3-step gaussian pyramid (filtered with σ, √2σ, 2σ) of a 2D image using pseudo-code.
5.1.3. Given an image of size � × �, where � = 2�, what is the maximum number of levels you can have in an
approximation pyramid representation? (The maximum level is reached when the coarsest level has only 1 pixel).
What is the total number of pixels in the pyramid (i.e. including pixels at all pyramid levels)? How does this
number compare with the original number of pixels in the image? Since this number is larger than the original
pixel number, what are some of the benefits of using the approximation pyramid? (give some examples). Repeat
the step for the prediction residual pyramid. Display and discuss the results.
5.1.4. For the grayscale Lena image, manually compute a 3-level approximation pyramid and corresponding prediction
residual pyramid. Use 2x2 averaging for the approximation and use pixel replication for the interpolation filters.
5.1.5. For the grayscale Lena Image, compute the wavelet transform (with 3-level) using the Haar analysis filters.
Comment on the differences between the pyramids generated in Prob. 5.1.2 with the ones generated here.
5.1.6. Quantize all the wavelet coefficients (whole sub-bands) created in Prob. 5.1.3 by a step size of � = 2. Then
reconstruct the image from the quantized wavelet coefficients using Haar synthesis filter. Report PSNR values
and discuss the results.
�′(�, �) = � × ���[�(�, �)] × ����� [|�(��, �)|] , � represents the wavelet coefficient
Note: you can use dwt2, idwt2, and psnr functions for problems 5
