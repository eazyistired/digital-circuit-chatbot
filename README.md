# digital-circuit-chatbot

# Initial setup:
``` git clone --recursive https://github.com/eazyistired/digital-circuit-chatbot.git ```

``` cd digital-circuit-chatbot ```

``` python -m venv venv ```

``` source venv/bin/activate ```

``` pip install -r requirements.txt ```

If you want to upload your own resources open *start_script.py* and change *COPY_RESOURCES* from *True* to *False*. And upload your questions in excel format under */database/questions/* and name it *questions.xlsx*. The excel header should contain the columns: **_Question, Answer, Context_**.

If you want to use shared resources leave it as it is. Be careful when using shared resources, if you change/delete something it affects all users.

``` python start_script.py ```

# Running the script :

``` cd digital-circuit-chatbot-api ```

If you brought your own resources go to *config.json* and change *convert_docs_to_database* from *false* to *true*.

If you want to type your questions in the terminal:
``` python main_api.py```

If you want to run on question database:
Go to *config.json* and set *ask_your_own_questions* to *false*.

``` python main_api.py > log.txt```

The results as well as the config object will be stored in *database/results/* folder.
