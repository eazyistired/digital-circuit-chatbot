# digital-circuit-chatbot

# Initial setup:

``` git clone --recursive https://github.com/eazyistired/digital-circuit-chatbot.git ```

``` python -m venv venv ```

``` source venv/bin/activate ```

``` pip install -r requirements.txt ```

If you want to upload your own resources open *start_script.py* and change *COPY_RESOURCES* from *True* to *False*. If you want to use shared resources leave it as it is. 
Be careful when using shared resources, if you change/delete something it affects all users.

``` python start_script.py ```

# Running with automated QA system from database/questions

``` cd digital-circuit-chatbot-api ```

``` python main_api.py > log.txt```