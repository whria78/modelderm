The algorithm (Model Dermatology) could diagnose 186 skin conditions. This is a lite version of ModelDerm Build2021 (EfficientNet Lite B0; CPU version). It can be use without any restriction.

# Model Dermatology API Example

Note) If too many calls come from the same IP address, it may be delayed or a "too many request" error may occur. It is preferable to call the API from the client side.

<pre><code>python3 modelderm_t.py
</code></pre>

At this moment, no metadata is required as following,
```
args2_='<id>image_id</id><race></race><birth></birth><sex></sex><location></location><pruritus></pruritus><pain></pain><onset></onset>'
```

Use a POST method to transfer up to 5 images. Please check the python example (PYTHON3). 

# Terms of Use
1) Free and no restriction
2) This is a lite version of ModelDerm Build2021.
3) Please do not submit images without permission of the original owner although we do not save the submitted images. 
4) We are not responsible for inaccurate result or technical problems (server down).
5) We do not store the submitted image.

# Authorization (API Key)
API Key = "test"

# Server Address
https://t.modelderm.com

# Web-DEMO
The realtime DEMO of the lite version is available at http://t.modelderm.com

# Algorithm
The algorithm has been developed and maintained by Han Seung Seog (I Dermatology).

```
Studies related with the algorithm
1. Assessment of Deep Neural Networks for the Diagnosis of Benign and Malignant Skin Neoplasms in Comparison with Dermatologists: A Retrospective Validation Study. PLOS Medicine, 2020
2. Performance of a deep neural network in teledermatology: a single‐center prospective diagnostic study. J Eur Acad Dermatol Venereol. 2020
3. Keratinocytic Skin Cancer Detection on the Face using Region-based Convolutional Neural Network. JAMA Dermatol. 2019
4. Seems to be low, but is it really poor? : Need for Cohort and Comparative studies to Clarify Performance of Deep Neural Networks. J Invest Dermatol. 2020
5. Multiclass Artificial Intelligence in Dermatology: Progress but Still Room for Improvement. J Invest Dermatol. 2020
6. Augment Intelligence Dermatology : Deep Neural Networks Empower Medical Professionals in Diagnosing Skin Cancer and Predicting Treatment Options for 134 Skin Disorders. J Invest Dermatol. 2020
7. Interpretation of the Outputs of Deep Learning Model trained with Skin Cancer Dataset. J Invest Dermatol. 2018
8. Automated Dermatological Diagnosis: Hype or Reality? J Invest Dermatol. 2018
9. Classification of the Clinical Images for Benign and Malignant Cutaneous Tumors Using a Deep Learning Algorithm. J Invest Dermatol. 2018
10. Augmenting the Accuracy of Trainee Doctors in Diagnosing Skin Neoplasms in a Real-World Setting: A Prospective Before and After Study. PLOS One, 2022
11. Evaluation of Artificial Intelligence-assisted Diagnosis of Skin Neoplasms – a single-center, paralleled, unmasked, randomized controlled trial. J Invest Dermatol. 2022
```

# Contact
I hope the algorithm to be widely used in other applications. Please contact to Dr. Han Seung Seog (whria78@snu.ac.kr) 