
MESSAGES=[
    {"role": "developer", "content": [
        {
            "type": "text", 
            "text": f"Do not add formatting elements to responses"
        },
        {
            "type": "text", 
            "text": f"Always send the response in json format. The json will have just one dictionary consisting of two elements: 'chat' and 'model. The model element shall be a string containing the model in yaml. Use escaped line breaks to separate lines."
        },
        {
            "type": "text", 
            "text": f"The model shall always be at the end of the response."
        },
        {
            "type": "text", 
            "text": f"If not asked explicitly, the changes to current the model shall be incremental and posibly minimal with respect to the previous model."
        },
        {
            "type": "text", 
            "text": "The tomato model has a format of yaml file"
        },
        {
            "type": "text", 
            "text": "Top elements can be a single node 'global parameters' and a single node 'functions'. 'global parameter' is a list of parameters. 'function' is a list of functions."
        },
        {
            "type": "text", 
            "text": "Function can contain only element 'parameters' that is a list and may contain 'parameter', 'linked parameter' or 'output parameter'. "
        },
        {
            "type": "text", 
            "text": "'global parameters' that is a list and may contain 'parameter', 'linked parameter' or 'output parameter'. "
        },
        {
            "type": "text", 
            "text": "'linked parameter' has an obligatory element 'linked to' that is a string containing the name of a parameter from 'global parameters'."
        },
        {
            "type": "text", 
            "text": "'linked to' must not refer to a global parameter that is defined before the 'linked parameter'."
        },
        {
            "type": "text", 
            "text": "'linked to' must not refer to a sub-parameter of a global parameter"
        },
        {
            "type": "text", 
            "text": "global parameters shall contain only parameters that are used more than once in the model."
        },
        {
            "type": "text", 
            "text": "'parameter' may contain only 'parameters' or 'choices'. Not both at the same time."
        },
        {
            "type": "text", 
            "text": "'Only the top parameter list of a function may contain 'output parameter' elements."
        },
        {
            "type": "text", 
            "text": "'output parameter' has only other element: 'default value'."
        },
        {
            "type": "text", 
            "text": "'choices' is a list of possible values of a parameter. It may be expressed as a list of 'choice' elements or as a flow"
        },
        {
            "type": "text", 
            "text": "only allowed element of 'choices' list is 'choice'"
        },
        {
            "type": "text", 
            "text": "'choice' may have only one element: 'value'"
        },
        {
            "type": "text", 
            "text": """this is an example model:
global parameters:
- parameter: Weapon
  choices: [sword, bow, dagger]

functions:
- function: duel
  parameters: 
  - parameter: good guy
    choices: [Peter, Susan, Edmund, Lucy]
  - linked parameter: good guy's weapon
    linked to: Weapon
  - parameter: bad guy
    choices: [Jadis, Maugrim, a giant]
  - linked parameter: bad guy's weapon
    linked to: Weapon
"""
        },
        {
            "type": "text", 
            "text": """this is an example model:
global parameters:
- parameter: Weapon
  choices: [sword, bow, dagger]
- parameter: Character
  parameters:
  - parameter: name
    choices: [Peter, Susan, Edmund, Lucy]
  - parameter: gender
    choices: [F, M]
  - linked parameter: weapon
    linked to: Weapon

functions:
- function: duel
  parameters: 
  - linked parameter: contestant 1
    linked to: Character
  - linked parameter: contestant 2
    linked to: Character
"""
        },
        {
            "type": "text", 
            "text": """this is an example model:
functions:
- function: character
  parameters:
  - parameter: name
    choices: [Peter, Susan, Lucy, Edmund]
  - parameter: location
    choices: [Cair Paravel, Stone Table, Lantern Waste]
  - parameter: weapon
    choices: 
    - choice: sword
    - choice: bow
    - choice: dagger
"""},

    ]},
]
