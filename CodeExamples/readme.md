## GitHub account
* [Join GitHub](https://github.com/join) 
* [GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart)

## OpenAI account
* [Join OpenAI](https://platform.openai.com/signup)
* [Developer quickstart](https://platform.openai.com/docs/quickstart?context=python)

## Hugging Face account
* [Join Hugging Face](https://huggingface.co/join)

## Setting up a Python environment using conda
Here's how you can create a Python 3.10 environment:

* Create a Python 3.10 environment:
```
conda create --name project python=3.10
conda env list
```
* Activate the environment:
```
conda activate project
```
* Deactivate the environment:
```
conda deactivate
```
* Install Python libraries:
```
pip install numpy
pip install matplotlib
pip install pandas
pip install beautifulsoup4
```

or

```
pip install -r requirements.txt
```

* Lists all the packages installed in the currently active conda environment.
```
conda list
```
or use grep to search for a specific package
```
conda list | grep numpy
```
