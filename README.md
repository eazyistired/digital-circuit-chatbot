# digital-circuit-chatbot

# Initial setup:
``` git clone --recursive https://github.com/eazyistired/digital-circuit-chatbot.git ```

``` cd digital-circuit-chatbot ```

``` python -m venv venv ```

``` source venv/bin/activate ```

``` pip install -r requirements.txt ```

``` python initial_script.py ```

# Running the app :

### Create knowledge database

Add the .pdf files that you want to use as knowledge database in the *project_directory*/*database* folder. 

### Change LLM - optional, we recommend you stick with the default one

By default the assistant will use the llama-2-13b-chat as Large Language Model, if you want to choose another one you can pick from one of the models already located under *project_directory*/*models* or download another one from Hugging Face and copy it in the *models* directory. If you decided to change the default LLM, you simply have to copy the name of the directory that the new llm is stored under: e.g. *mistral-7b-instruct-v2* go to *project_directory*/*digital-circuit-chatbot-api*/*config.json* and set the *llm_model_name* parameter to the new one.

### Activate the python virtual environment

```source venv/bin/activate```

### Start the app

``` python app.py ```

Visual Studio Code should prompt you to open the app in an external browser, click that.