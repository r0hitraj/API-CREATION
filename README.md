# API-CREATION

Problem Statement:
You have to create a Django application which should be able to store information about different types of Pizza,
 then create an API interface that lists the information about all the different stored pizzas, and also be able to interact with that information (such as edit or delete).

Database
MongoDB should be configured with the project. Our database should be able to store information about Pizza, following are the details:
•	A Pizza can be of multiple types: Regular or Square
•	A Pizza can be of multiple sizes: Small, Medium, Large, etc. (These are just examples; the user should be allowed to add any other size at any point of time)
•	A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.), the choice of toppings should not be limited to 
		the ones mentioned above, the user should be allowed to add any type of topping at any point of time)

API
•	Create an API endpoint to create regular pizza and a square pizza.
•	Create an API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
•	Allow filtering the list of pizza returned by the API based on Size & Type of    Pizza.
•	Create an API endpoint that allows the user to edit or delete any pizza from the database.

Errors & Validation
•	The API should return proper 40x codes when any kind of wrong input is sent to the API, the server should not return 500 errors
•	The user should not be able to create a pizza of any other type except Regular and Square.
•	The user should not be able to create pizza of size which isn't present in the database.

### some tools require  to run the project:
1. Mongodb
2. I have chossen windows system for development

### Steps to run the project:
step1->git clone https://github.com/r0hitraj/API-CREATION.git
<br>
step2->install virtual env  by -> mkvirtualenv [any name]   //note here any-name is not in bracket this is used only for the refrence instead of it use your suitable name
<br>
step3-> workon [any name] <br>
step4-> pip install -r requirements.txt <br>
step5->python manage.py migrate <br>
step6->python manage.py runserver  <br>

### now Start testing

### Api Endpoints:



<h1> GET</h1>
# Fiter by Pizza size and type

    GET /api/pizza/?pizza_type=regular&pizza_size=small
    
Returns a list of filtered pizza.

## Parameters

### URL Parameters
Field  | Type |Description
---  | --- | ---
pizza_type | String |Type of Pizza to be filtered with (eg:- Regular or square)
pizza_size  | String |Size of Pizza to be filtered with  (eg:- small, large, etc)

If one of them is provided like `` /api/pizza/?pizza_type=regular`` then also it will work server will not send error.

## Example
### Request

    GET http://localhost:8000/api/pizza/?pizza_type=regular&pizza_size=small

### Response
``` json
{
    "filter_paramters": [
        "pizza_size",
        "pizza_type"
    ],
    "filter_value": [
        "small",
        "regular"
    ],
    "filter_pizza_result_count": 3,
    "filter_pizza_result": [
        {
            "id": 9,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": []
        },
        {
            "id": 10,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": [
                {
                    "id": 8,
                    "topping": "Capsicum"
                },
                {
                    "id": 9,
                    "topping": "Tomato"
                }
            ]
        },
        {
            "id": 15,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": []
        }
    ]
}
```
### If there is no result in database matching the filters then server will return an empty array 
### Request

    GET http://localhost:8000/api/pizza/?pizza_type=regula

### Response# Display Pizza By ID

    GET /api/pizza/:pizza_id/
    
Returns a pizza by id.

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

## Example
### Request

    GET http://localhost:8000/api/pizza/10/

### Response
``` json
{
    "success": "Pizza Exists",
    "pizza": {
        "id": 10,
        "pizza_type": "Regular",
        "pizza_size": {
            "id": 1,
            "pizza_size": "Small"
        },
        "pizza_toppings": [
            {
                "id": 8,
                "topping": "Capsicum"
            },
            {
                "id": 9,
                "topping": "Tomato"
            }
        ]
    }
}
```
### Error
#### If pizza of mentioned id does not exist in Database then server repondes with a 400 Bad Request
### Response
``` json
{
    "error": "Pizza with specified id doesn't exist."
}
```
# Pizza Sizes List

    GET /api/pizza_size/
    
Returns a list of pizza sizes in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_size/

### Response
``` json
[# List Of Pizzas, Sizes, Types and Toppings

    GET /api/pizza/
    
Returns a list of Pizzas , sizes, types and toppings stored in Database.

## Example
### Request
    GET http://localhost:8000/api/pizza/

### Response
``` json
{
    "pizzas": [
        {
            "id": 1,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": [
                {
                    "id": 8,
                    "topping": "Capsicum"
                },
                {
                    "id": 9,
                    "topping": "Tomato"
                }
            ]
        }
    ],
    "pizza_sizes": [
        {
            "pizza_size": "Small"
        }
    ],
    "pizza_types": [
        "Regular",
        "Square"
    ]
}
```
# Pizza Toppings List

    GET /api/pizza_toppings/
    
Returns a list of pizza toppings in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_toppings/

### Response
``` json
[
    {
        "topping": "Tomato"
    },
    {
        "topping": "Capsicum"
    }
]
```
    {
        "pizza_size": "Large"
    },
    {
        "pizza_size": "Medium"
    },
    {
        "pizza_size": "Small"
    }
]
```# List Of Pizzas, Sizes, Types and Toppings

    GET /api/pizza/
    
Returns a list of Pizzas , sizes, types and toppings stored in Database.

## Example
### Request
    GET http://localhost:8000/api/pizza/

### Response
``` json
{
    "pizzas": [
        {
            "id": 1,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": [
                {
                    "id": 8,
                    "topping": "Capsicum"
                },
                {
                    "id": 9,
                    "topping": "Tomato"
                }
            ]
        }
    ],
    "pizza_sizes": [
        {
            "pizza_size": "Small"
        }
    ],
    "pizza_types": [
        "Regular",
        "Square"
    ]
}
```
# Pizza Toppings List

    GET /api/pizza_toppings/
    
Returns a list of pizza toppings in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_toppings/

### Response
``` json
[
    {
        "topping": "Tomato"
    },
    {
        "topping": "Capsicum"
    }
]
```
``` json
{
    "filter_paramter": "pizza_type",
    "filter_value": "regula",
    "filter_pizza_result": []
}
```
# Display Pizza By ID

    GET /api/pizza/:pizza_id/
    
Returns a pizza by id.

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

## Example
### Request

    GET http://localhost:8000/api/pizza/10/

### Response
``` json
{
    "success": "Pizza Exists",
    "pizza": {
        "id": 10,
        "pizza_type": "Regular",
        "pizza_size": {
            "id": 1,
            "pizza_size": "Small"
        },
        "pizza_toppings": [
            {
                "id": 8,
                "topping": "Capsicum"
            },
            {
                "id": 9,
                "topping": "Tomato"
            }
        ]
    }
}
```
### Error
#### If pizza of mentioned id does not exist in Database then server repondes with a 400 Bad Request
### Response
``` json
{
    "error": "Pizza with specified id doesn't exist."
}
```
# Pizza Sizes List

    GET /api/pizza_size/
    
Returns a list of pizza sizes in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_size/

### Response
``` json
[
    {
        "pizza_size": "Large"
    },
    {
        "pizza_size": "Medium"
    },
    {
        "pizza_size": "Small"
    }
]
```# List Of Pizzas, Sizes, Types and Toppings

    GET /api/pizza/
    
Returns a list of Pizzas , sizes, types and toppings stored in Database.

## Example
### Request
    GET http://localhost:8000/api/pizza/

### Response
``` json
{
    "pizzas": [
        {
            "id": 1,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": [
                {
                    "id": 8,
                    "topping": "Capsicum"
                },
                {
                    "id": 9,
                    "topping": "Tomato"
                }
            ]
        }
    ],
    "pizza_sizes": [
        {
            "pizza_size": "Small"
        }
    ],
    "pizza_types": [
        "Regular",
        "Square"
    ]
}
```
# Pizza Toppings List

    GET /api/pizza_toppings/
    
Returns a list of pizza toppings in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_toppings/

### Response
``` json
[
    {
        "topping": "Tomato"
    },
    {
        "topping": "Capsicum"
    }
]
```

<hr>
<h1> POST </h1>
# Create Pizza

    POST /api/pizza/
    
Create a Pizza. Returns the newly-created object.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
pizza_type | Y| String | Type of pizza (It can only be Regular or Square)
pizza_size | Y |String| Size of pizza (eg:- small, large, etc)
toppings | N | Array | Toppings to put on pizza (eg:- capsicum, etc). There can be multiple toppings

## Example
### Request

    POST http://localhost:8000/api/pizza/
#### Request Body
```json 
{
	"pizza_type":"Regular",
	"pizza_size":"small",
	"toppings":[
		{
			"topping":"Capsicum"
		},
		{
			"topping":"Tomato"
		}
	]
}
```
### Response
``` json
{
    "new_pizza": {
        "id": 16,
        "pizza_type": "Regular",
        "pizza_size": {
            "id": 1,
            "pizza_size": "Small"
        },
        "pizza_toppings": [
            {
                "id": 8,
                "topping": "Capsicum"
            },
            {
                "id": 9,
                "topping": "Tomato"
            }
        ]
    }
}
```

### Error
#### If anything other than Regular or Square is passed for pizza_type
``` json
{
    "error": "Please provide correct pizza_type",
    "correct_type_choices": [
        "Regular",
        "Square"
    ]
}
```
#### If pizza_size is not present in database
``` json
{
    "error": "Please provide correct pizza_size",
    "correct_size_choices": [
        {
            "pizza_size": "Small"
        },
        {
            "pizza_size": "Large"
        },
        {
            "pizza_size": "Medium"
        }
    ]
}
```

#### If topping is not present in database
``` json
{
    "error": "Please enter correct topping. (cap) is not a valid  topping.",
    "correct_topping_choices": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```# Create Pizza Size

    POST /api/pizza_size/
    
Create a new Pizza Size.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
pizza_size | Y |String| Size of pizza (eg:- small, large, etc)

## Example
### Request

    POST http://localhost:8000/api/pizza_size/
### Request Body
```json 
{
    "pizza_size": "Medium"
}
```
### Response
``` json
{
    "new_pizza_size": {
        "pizza_size": "Medium"
    }
}
```

### Error
#### If Size already existing in Database
``` json
{
    "error": "(New) a# Create Pizza Toppings

    /api/pizza_toppings/
    
Create a new Pizza Topping.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
topping | Y |String| Topping of pizza (eg:- capsicum, tomato, etc)

## Example
### Request

    POST http://localhost:8000/api/pizza_toppings/
#### Request Body
```json 
{
    "topping": "onion"
}
```
### Return
``` json
{
    "new_topping": {
        "topping": "Onion"
    }
}
```

### Error
#### If Topping already existing in Database
``` json
{
    "error": "(Capsicum) already exists in system",
    "topping_existing": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```lready exists in system",
    "pizza_size_existing": [
        {
            "pizza_size": "Small"
        },
        {
            "pizza_size": "New"
        }
    ]
}
```# Create Pizza Toppings

    /api/pizza_toppings/
    
Create a new Pizza Topping.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
topping | Y |String| Topping of pizza (eg:- capsicum, tomato, etc)

## Example
### Request

    POST http://localhost:8000/api/pizza_toppings/
#### Request Body
```json 
{
    "topping": "onion"
}
```
### Return
``` json
{
    "new_topping": {
        "topping": "Onion"
    }
}
```

### Error
#### If Topping already existing in Database
``` json
{
    "error": "(Capsicum) already exists in system",
    "topping_existing": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```


<hr>
<h1> PUT </h1>
# Update Pizza

    PUT /api/pizza/:pizza_id/
    
Update a Pizza

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
pizza_type | N | String | Type of pizza (It can only be Regular or Square)
pizza_size | N |String| Size of pizza (eg:- small, large, etc)
toppings | N | Array | Toppings to put on pizza (eg:- capsicum, etc). There can be multiple toppings

## Example
### Request

    PUT http://localhost:8000/api/pizza/16/
#### Request Body
```json 
{
	"pizza_type":"Square",
	"pizza_size":"small",
	"toppings":[
		{
			"topping":"Capsicum"
		},
		{
			"topping":"Tomato"
		}
	]
}
```
### Return
``` json
{
    "success": "Pizza Updated Successfully",
    "updated_pizza": {
        "id": 16,
        "pizza_type": "Square",
        "pizza_size": {
            "id": 1,
            "pizza_size": "Small"
        },
        "pizza_toppings": [
            {
                "id": 8,
                "topping": "Capsicum"
            },
            {
                "id": 9,
                "topping": "Tomato"
            }
        ]
    }
}
```

### Error
#### If anything other than Regular or Square is passed for pizza_type
``` json
{
    "error": "Please provide correct pizza_type",
    "correct_type_choices": [
        "Regular",
        "Square"
    ]
}
```
#### If pizza_size is not present in database
``` json
{
    "error": "Please provide correct pizza_size",
    "correct_size_choices": [
        {
            "pizza_size": "Small"
        },
        {
            "pizza_size": "Large"
        },
        {
            "pizza_size": "Medium"
        }
    ]
}
```

#### If topping is not present in database
``` json
{
    "error": "Please enter correct topping. (cap) is not a valid  topping.",
    "correct_topping_choices": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```
<hr>
<h1> DELETE </h1>


    DELETE /api/pizza/:pizza_id/
    
Delete Pizza of specified ID.

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

## Example
### Request

    DELETE http://localhost:8000/api/pizza/9/

### Response
``` json
{
    "success": "Pizza Deleted"
}
```

### Error
#### If pizza of mentioned id does not exist in Database then server repondes with a 400 Bad Request
### Response
``` json
{
    "error": "Pizza with specified id doesn't exist."
}
```
