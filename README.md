# maria

Maria is an innovative chatbot designed by Udana Wimukthi, founder and CEO of Gapi Dream Company, to provide companionship and support to those who may find themselves alone, including the elderly and individuals without immediate family care. Developed in Python and currently under development, Maria utilizes the LM Studio API for text completion and the Open Voice GradEO client for text-to-speech functionalities. The system is engineered to engage users in seamless conversation, automatically detecting when a user starts or stops talking, transcribing their speech, and replying vocally. Aimed at fostering connection and accessibility, Maria stands out as a compassionate assistant for those in need of company. This program is released under the MIT License, emphasizing its non-commercial use. Maria symbolizes Gapi Dream Company's commitment to leveraging technology for social good, bridging gaps between people and technology with empathy and innovation.

## how to install 

in order to install 
1. we recommend using anaconda as the virtual environment ( this step is optional )
2. clone the repository
3. creat a virtual environment with python 3.10 `conda create -n maria python=3.10 -y`
4. install the requirements `pip install -r requirements.txt`
5. Install LM Studio and download your favorite LLm ( we recommend Mistral 7b, Zephyr Alpha 7b )
6. Install Open Voice with its Gradio interface ( we recommend using Pinokio. It makes the installation process a lot easier )

## how to run

1. you have to run LM studio and start a server with your favorite LLM.
2. then you have to start opening the voice
3. then navigate to the location where you clone the repo and run  `python main.py` in the cmd or the virtual environment you created.
4. then you can keep talking

## customize

you can customize the program by changing the system prompt.
