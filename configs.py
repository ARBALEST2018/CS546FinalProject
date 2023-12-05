OPENAI_API_KEY = "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"
OPENAI_CHAT_MODEL = "gpt-4-1106-preview"
# "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"
OPENAI_TEXT_MODEL = "text-davinci-003"
EVENT_EXT = "What is the event in this sentence? Define it with one word."
ARGUMENT_EXT = "This sentence describes an event. What arguments of this event are mentioned in this sentence? List them one by one concisely in format: \"argument type: argument content\""

PROMPT_0 = "Here are some examples of event arguments. Text and event arguments are provided. Each event argument consists of event argument type, event argument content, and event argument location. Event argument contents are quoted from the text. Event argument locations are the index or position of the first word of that event argument content in the text."
PROMPT_1 = "Based on the shown example above, extract the event arguments from the text below. The event argument types are given, please choose the appropriate phrase from the text to match each argument, and provide the location index of you choice. Remember that the number of argument contents are the same as the number of argument types that are provided, and each event argument location is the index or position of the first word of that event argument content in the text."
PROMPT_0_NL = "Here are some examples of event arguments. Text and event arguments are provided. Each event argument consists of event argument type and event argument content. Event argument contents are quoted from the text. Each event argument type match one and only one event argument content."
PROMPT_1_NL = "Based on the shown example above, extract the event arguments from the text below. The event argument types are given, please choose the appropriate phrase from the text to match each argument. Please only answer the given argument types Remember that the number of argument contents are the same as the number of argument types that are provided."
PROMPT_TEXT = "Text "
PROMPT_EVENT_TYPE = "Event type "
PROMPT_EVENT_ARGUMENT_TYPE = "Event argument types "
PROMPT_EVENT_ARGUMENT_CONTENT = "Event arguments contents "
PROMPT_EVENT_ARGUMENT_LOCATION = "Event argument locations "

INSTRUCTION_HEAD = "# Instruction"
INSTRUCTION_TEMPLATE = "Given the document, extract the information based on the corresponding template with arguments in JSON format. \n"+"Fill the arguments with entity you find in the document. \n"+"Only one entity from the given document is sufficient. Choose the most relevant based on the context of the document.\n"+"If no such argument found, you can fill with <UNK> notation."
INSTRUCTION_SAMPLE = "The following examples is how you should perform a multi-sentence information extraction tasks.\n"+"Your tasks is to fill the arguments with entities you extract from the user input documents in JSON format.\n"+"You can use <UNK> to indicate the unknown entity.\n"+"Answer the arguments in a consistent style as the example."
EXAMPLE_HEAD = "# Example"
EXAMPLE_DOCUMENT_HEAD = "## Document"
EXAMPLE_ANSWER_HEAD = "## Answer"

DOCUMENT_HEAD = "# Document"
TEMPLATE_HEAD = "# Template"
TASK_HEAD = "# Task"
TASK = "Extract the arguments from the document in JSON format:"


# # Instruction
# The following examples is how you should perform a multi-sentence information extraction tasks.
# Your tasks is to fill the arguments with entities you extract from the user input documents.
# You can use <UNK> to indicate the unknown entity.
# Answer the arguments in a consistent style as the example.

# # Example
# ## Document
# Transportation officials are urging carpool and teleworking as options to combat an expected flood of drivers on the road.
# ( Paul Duggan)
# -- A Baltimore prosecutor accused a police detective of “ sabotaging ” investigations related to the death of Freddie Gray, accusing him of fabricating notes to suggest that the state ’s medical examiner believed the manner of death was an accident rather than a homicide.
# The heated exchange came in the chaotic sixth day of the trial of Baltimore Officer Caesar Goodson Jr., who drove the police van in which Gray suffered a fatal spine injury in 2015.
# ( Derek Hawkins and Lynh Bui)

# ## Answer
# <arg1> killer(person/organisation/country): Officer Caesar Goodson Jr.
# <arg2> victim(person): Freddie Gray
# <arg3> instrument(vehicles/explosives/sharps/blunts/firearms/chemicals): <UNK>
# <arg4> place:Baltimore