Overview
========
This package is designed to automate report writing in natural language based on specificly defined criteria for each report. The project is not yet well-documented because it is in active development.

Usage
=====
The most basic usage is demonstrated with a working example in the `workingExample` directory. That program can be run as is to generate output using one of the included snippets from the `lib` directory.

In general, the end user will need to write two different pieces of code (a script and a snippet) and supply subject data.

Writing a Script
----------------
The script is generally fairly basic and will closely follow the structure of the working example. (In fact copying the working example is a good place to start.) The most common modification to the basic script is to put the output to use in some interesting way.

Writing a Snippet
-----------------
In most cases, the snippets provided in the lib directory will be helpful, but not sufficient on their own and you will need to write your own snippet. All snippets extend the general Snippt class either directly (most common in my own usage) or indirectly in the usual OOP way. A good way to start a snippet is to copy the blank template or an example from the lib directory.

All snippets must do the following:

1. Setup the init. Look through an existing one to document this better
2. Implement a genetate_text method
3. Implement token_(token name) methods for all tokens that whould be replaced directly in this method.

Subject Data
------------
Subject data is stored internally in a modified version of a `xml.etree.ElementTree`.

The `snippets.core.input` module provides methods to simplify inputting subject data from both CSV (simple cases) and XML (more complex or nested cases) files.

This document should be expanded to better document both of those methods.

If neither of those methods suites your needs, any manner of getting your data into the `ElementWrapper` format will do, but thorough documentation is beyond the scope of this document. See the source of `input.py` for details.

Processing Order
================
This section should probably have a better title.

When evaluating a snippet the following things happen:

1. The generate text method of the snippet is called
2. The tokens are replaced

replacing tokens
----------------
Tokens can be replaced in one of three ways
1. The token is passed to a child snippet
2. The token is implemented directly in this snippet (best used for simple cases).
3. The token is not directly replaced at all, but rather left to be replaced in a parent (or higher-order ancestor) snippet.

License
=======
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, we dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of my heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

For more information, please refer to <http://unlicense.org/>
