Start ECS using FunctionGraph and agency
========================================

.. toctree::
   :maxdepth: 3
   :includehidden:
   
Sample on how to start an ECS instance using an agency.

This sample show how to use functiongraph start an ECS instance using 
following credentials retrieved by the agency:


* context.getSecurityAccessKey()
* context.getSecuritySecretKey()
* context.getSecurityToken()


For complete source code, see :github_repo_master:`samples-doc/functiongraph/ecs<samples-doc/functiongraph/ecs>` on GitHub.

Deployment
----------

Build deployment zip
^^^^^^^^^^^^^^^^^^^^^^

To build the deployment zip, execute following command in
folder: **samples-doc/functiongraph/ecs**

.. code-block:: python

   python3 createZip.py


This will create **code.zip** in folder **target** with code and dependencies included.

Create FunctionGraph function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create function
*******************

Use `OpentelekomCloud FunctionGraph console <https://console.otc.t-systems.com/functiongraph/>`_ to create a function with following
settings:


**Create With**:  Create from scratch 

**Basic Information**

* **Function Type**  Event Function  
* **Region**  <YOUR REGION>  
* **Function Name** <YOUR FUNCTION NAME>  
* **Agency**  Specify an agency with policy to start ECS instance  
* **Runtime**  Python 3.10

Upload code
*******************

Use **Upload** -> **Local ZIP** and upload *code.zip* from previous step.

Configure function
*******************

In **Configuration** -> **Basic Settings** -> **Handler**:   *src/ecs_sample.handler*

In **Configuration** -> **Environment Variables** add following variables:

.. list-table:: Environment variables
    :widths: 20 20 25
    :header-rows: 1

    * - Environment variable name
      - Value
      - Default

    * - INSTANCE_ID
      - <ID of ecs instance>
      - 

    * - ECS_ENDPOINT
      - <ecs endpoint>
      - Default: ecs.eu-de.otc.t-systems.com , :otc_docs:`Regions and Endpoints<regions-and-endpoints/index.html>`


Create Test Event
*******************

In **Code** create a Test Event using "Blank Template" (Event is not used in function)

Test function
^^^^^^^^^^^^^^^

Click **Test** to test function.

