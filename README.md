![readmebanner]()

___

<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#project-planning)]
[[Key Findings](#key-findings)]
[[Take Aways](#take-aways)]
[[Data Dictionary](#data-dictionary)]
[[Repo Replication](#repo-replication)]

___
<a name="project-summary"></a><h1><img src=""/></h1>



Using Pandas, Mathplotlib, and SciKit-Learn in Jupyter Lab, I prepped and explored strings of text scraped from Google's Github Repositories to create a model that predicted the primary coding language used in that repository.
# <span style="color:red">add final prediction results</span>



<a name="project-planning"></a><h1><img src=""/></h1>
### Goal: 
The goal for this project is to create a model that will accurately predict the primary coding language of a Github Repository given text from a `README`.

### Initial Hypotheses:

> Hypothesis₁
>
> There is a relationship between mention of programming language in `README` and primary coding language used.
    
> Hypothesis₂
>
> `README` text length does **not** affect the programming language.

    
### Project Planning Initial Thoughts:
**First iteration:**
I'd like my first iteration to include a second feature of `README` length. 

**Second iteration:**
I'd like to use takeaways from my exploration to create another useful feature.

**Deliverables:**
- Final clean, interactive Py notebook.
- Presentation Slide Deck

    
    
[Jump to Navigation](#navigation)

<a name="key-findings"></a><h1><img src=""/></h1>

## Exploration Key Findings:
### Univariate




    
[Jump to Navigation](#navigation)

<a name="take-aways"></a><h1><img src=""/></h1>

- 
- 



[Jump to Navigation](#navigation)

<a name="data-dictionary"></a><h1><img src=""/></h1>

| column_name     | description                                                           | key                          | dtype  |
|-----------------|-----------------------------------------------------------------------|------------------------------|--------|
| `repo`          | Link suffix in `username`/`repo_name` formatting.                     |                              | object |
| `language`      | Primary coding language used in the repo.                             |                              | object |
| `readme_contents`| String of test scraped from repo's README file.                      |                              | object |
| ``           |                                  |                              |   |





[Jump to Navigation](#navigation)

<a name="repo-replication"></a><h1><img src=""/></h1>

In order to get started reproducing this project, you'll need to setup a proper environment.

1. Begin by downloading the weather data [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).
![aacbanner](https://i.pinimg.com/originals/de/1b/51/de1b51677d5511963d8db44b964c6fbe.png)    







2. Recover your downloaded zip file and unzip.

**Prep your repo.**

3. Create a new repo to house this project, and clone it into your terminal by copying the SSH link:
    ![prep your repo]()
> <code>git clone </code> (Cmd+V)
    

4. Create a `.gitignore` that includes any files you dont want shared on the internet and **push it**! 
    
    - (This can include your newly downloaded .csv files)
> <code>code .gitignore</code>



5. Create a `README.md` file to begin notating steps taken so far.
    
><code>code README.md</code>


6. Transfer your unzipped .csv files into your newly established folder.


7. Create a Jupyter Lab environment to continue working in.
> <code>jupyter lab</code>


8. Create Jupyter Notebook to begin the data pipeline. 

![jlablauncher](https://i.pinimg.com/originals/98/92/c5/9892c5042934750b5ba073f2d49f6184.png)
    




[Jump to Navigation](#navigation)








































