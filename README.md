# ril-cli

## How to use

* **IMPORTANT:**
    * You must have python and the corresponding libraries installed to run this script.
        * If you have Conda installed, simply run ```conda env create -f ril-cli.yml``` to create an environment with
          the required dependencies.
    * Familiarize yourself with the Qualtrics form so that you know what inputs you should have in your files.
* Create a .txt file with your name, community name, and building name, all according to the form and each on a separate
  line.
* Then, use the interactions CSV template to compile your interactions (make sure to save this as a CSV).
* Finally, use the following command to run the script with your files (all files should be in the same directory as the
  script):
    * ```python rli_cli.py [your_text_file_name].txt [your_interactions_file_name].csv```
    * If the script fails to run a couple of times, don't worry, it will eventually run smoothly.
    * If the script submits one log successfully, then it has always submitted the subsequent logs successfully as well.
    * This script takes around 12-16 secs to submit each interaction, which is blazing fast compared to manual entry.
    * However, if the script doesn't work as stated above, please create a new GitHub issue.