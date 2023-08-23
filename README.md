# Hume AI - Expressive Prompt Engineering (EPE)

Our Expressive Prompt Engineering tool provides the Language-based Emotion Expression
Description (LEED) functionality which utilizes emotion scores from the Hume API and transforms them into descriptive text.  In this example code, we provide functionality for extracting emotion scores from a audio file using Hume's expressive speech prosody model, and from an image using Hume's facial expression model via our [SDK](https://github.com/HumeAI/hume-python-sdk). 

We also integrate the option to extract language embeddings from the LEED using OpenAI's Ada model, as well as prompting ChatGPT with an expression enhanced prompt. 

## Prerequisites

Make sure you have the following tools installed on your system:

- Anaconda or Miniconda
- Python 3.9
- pip (included with conda)

For this tool to use ChatGPT you will need access to **GPT-4**

## Installation Steps

Follow the steps below to set up and activate a Python environment for HumeE2T:

1. `conda create --name humeEPE python=3.9` (This creates a new conda environment named 'humeEPE' with Python 3.9)
2. `conda activate humeEPE` (This activates the 'humeEPE' environment)

Next, install the required Python packages using the provided `requirements.txt` file:

3. `pip install -r requirements.txt`

## Configuration

To access resources relating to HumeAI and OpenAI, you need to configure the API keys:

1. Find the API Key for HumeAI and in your terminal set the following:
	- `export HUME_API_KEY=<API_KEY>`
2. (Optional) In OpenAIConfigs `configs.py`, you can switch the embedding extraction (`EXTRACT_EMBEDDINGS`) to True in order to store embeddings. In this case you will also need you OpenAI API Key: 
    - `export OPENAI_API_KEY=<API_KEY>`
3. (Optional) If you want to prompt ChatGPT with expression enhanced prompt, you can also switch `PROMPT_CHATGPT` to True and alter the example `PROMPT` in `OpenAIConfigs`. 
4. In `configs.py` add the location of your file to `DATA_URLS`. For `prosody` this needs to be a `.wav` audio file, and for `face` this should be a `.png` image. 

## Usage

1. Run the main script with the command: `python main.py`

The example uses either a single audio file, or image file. See the [HumeAI SDK](https://github.com/HumeAI/hume-python-sdk) for more details on the various output option and available models. 

##  Citation:

[Brooks, J A](https://scholar.google.com/citations?user=89byC1UAAAAJ&hl=en&authuser=1)., [Tiruvadi, V](https://scholar.google.de/citations?user=BCPLyVwAAAAJ&hl=en&authuser=1&oi=ao)., [Baird, A](https://scholar.google.de/citations?user=fHQwc60AAAAJ&hl=en&authuser=1)., [Tzirakis, P](https://scholar.google.de/citations?user=rWKaCDAAAAAJ&hl=en&authuser=1)., [Li, H](https://scholar.google.de/citations?hl=en&authuser=1&user=QqpAM60AAAAJ)., [Gagne, C](https://scholar.google.de/citations?user=E6DqS3UAAAAJ&hl=en&authuser=1)., Oh, M., & [Cowen, A](https://scholar.google.de/citations?user=-i9gbsAAAAAJ&hl=en&authuser=1). "Emotion Expression Estimates to Measure and Improve Multimodal Social-Affective Interactions". (to appear) The ICMI, 4TH Workshop On Social Affective Multimodal Interaction for Health (SAMIH), 2023. 

## Hume AI Research Team
<table>
  <tr>
    <td align="center">
      <b>Jeff Brooks</b><br/><br/>
        <a href="https://github.com/jeffreyallenbrooks">  
        <img src="https://avatars.githubusercontent.com/u/11932562?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.com/citations?user=89byC1UAAAAJ&hl=en&authuser=1">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
    <td align="center">
        <b>Vineet Tiruvadi</b><br/><br/>
        <a href="https://github.com/virati">  
        <img src="https://avatars.githubusercontent.com/u/4741285?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?user=BCPLyVwAAAAJ&hl=en&authuser=1&oi=ao">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
    <td align="center">
        <b>Alice Baird</b><br/><br/>
        <a href="https://github.com/aliceebaird">  
        <img src="https://avatars.githubusercontent.com/u/10690171?v=4?s=100" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?user=fHQwc60AAAAJ&hl=en&authuser=1">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
    <td align="center">
        <b>Panagiotis Tzirakis</b><br/><br/>
        <a href="https://github.com/tzirakis">  
        <img src="https://avatars.githubusercontent.com/u/22793027?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?user=rWKaCDAAAAAJ&hl=en&authuser=1">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
  </tr>
  <tr>
    <td align="center">
        <b>Haoqi Li</b><br/><br/>
        <a href="https://github.com/haoqi">  
        <img src="https://avatars.githubusercontent.com/u/5073714?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?hl=en&authuser=1&user=QqpAM60AAAAJ">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
    <td align="center">
        <b>Chris Gagne</b><br/><br/>
        <a href="https://github.com/crgagne">  
        <img src="https://avatars.githubusercontent.com/u/10283088?v=4?s=100" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?user=E6DqS3UAAAAJ&hl=en&authuser=1">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
    <td align="center">
        <b>Moses Oh</b><br/><br/>
        <a href="https://github.com/Moses0h">  
        <img src="https://avatars.githubusercontent.com/u/30419922?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <!-- <a href="">
        <sub><b>Google Scholar</b></sub></a><br/> -->
    </td>
    <td align="center">
        <b>Alan Cowen</b><br/><br/>
        <a href="https://github.com/alanscowen">  
        <img src="https://avatars.githubusercontent.com/u/55813686?v=4" width="100px;" alt=""/>
        <br/><sub><b>Github</b></sub></a><br/>
        <a href="https://scholar.google.de/citations?user=-i9gbsAAAAAJ&hl=en&authuser=1">
        <sub><b>Google Scholar</b></sub></a><br/>
    </td>
  </tr>
</table>

