# Instagram Analysis 

Using artificial intelligence computer vision to go through all images of [Uli's Instagram timeline](http://www.instagram.com/cosmicrenaissance/) and get information about the visual content. What does the computer 'think' it 'sees' on each photo, what description and tags does it come back with?

Here is a visual representation of a quantitative analysis of the tags the machine came up with, for a more accurate result we should probably only use data where the confidence level is > 75%  

[![](http://cdn.sotong.io/insta/result.png)](http://cdn.sotong.io/insta/result.png) 

* * *

**Toolkit**  

o) [Microsoft Cognitive Services - Computer Vision](http://www.microsoft.com/cognitive-services/en-us/computer-vision-api)  
o) Python, Bash, ImageMagick  
o) [wordcloud](http://github.com/amueller/word_cloud)  

* * *

**Instagram Photo Data - Sunday, March 26th 2017**  

The output is sorted by the confidence level of the computer vision service, where a value between 0.9 and 1.0 reflects a scenario where the machine is extremely 'sure' that the analysis is correct. As you scroll down the page you should see that most results are getting less accurate - with some surprises in it as well..

![](http://cdn.sotong.io/insta/b2ad7a8487bcd4e577061b124a60f25f.jpg)  
**Text:** "a white plate topped with meat and veggies"  
**Confidence**: 0.9602044338155244  
**Tags**: "plate" "food" "table" "white" "indoor" "sitting" "meat" "top" "salad" "small" "bowl" "filled" "wooden" "green" "laying" "soup"

* * *

![](http://cdn.sotong.io/insta/85cde2ca2dcb18fc5932352003c6f8e5.jpg)  
**Text:** "a plate of food and a bowl of salad"  
**Confidence**: 0.9543408131595036  
**Tags**: "food" "table" "plate" "bowl" "sitting" "wooden" "meal" "salad" "red" "meat" "filled" "top" "glass" "different" "side" "rice" "fruit" "sandwich" "water"

* * *

![](http://cdn.sotong.io/insta/aff65e13ce6c18256d63822246aab2f1.jpg)  
**Text:** "a bowl filled with different types of food on a table"  
**Confidence**: 0.9497088126362747  
**Tags**: "plate" "food" "table" "different" "indoor" "bowl" "filled" "full" "holding" "several" "small" "tray" "sitting" "many" "topped" "dish" "variety" "set" "arranged" "various" "meat" "wooden" "bunch" "group" "salad"

* * *

![](http://cdn.sotong.io/insta/d98873dbc4802bd563ee4d9a482f04f8.jpg)  
**Text:** "a bowl filled with different types of food on a table"  
**Confidence**: 0.9457939301759611  
**Tags**: "food" "plate" "table" "bowl" "cup" "sitting" "filled" "coffee" "fruit" "meal" "various" "different" "salad" "sandwich" "top" "several" "holding" "wooden" "white" "banana" "cake" "large" "soup"

* * *

![](http://cdn.sotong.io/insta/3748eb3de114f971580ae7aaf9bbc464.jpg)  
**Text:** "a bowl of soup"  
**Confidence**: 0.9436335161256404  
**Tags**: "food" "table" "bowl" "plate" "cup" "soup" "filled" "sandwich" "sitting" "fruit" "eaten" "sauce" "bread" "top" "banana" "white" "cheese"

* * *

![](http://cdn.sotong.io/insta/02c32274ee5ee0366810001c1c879aa3.jpg)  
**Text:** "a group of people walking on a city street filled with traffic at night"  
**Confidence**: 0.9430423565338475  
**Tags**: "building" "outdoor" "street" "people" "city" "walking" "person" "sign" "night" "many" "busy" "group" "large" "crowded" "filled" "area" "crowd" "pedestrians" "bunch" "tall" "standing" "woman" "holding" "riding" "traffic" "man"

* * *

![](http://cdn.sotong.io/insta/0205a698b9693d348ca0ab504225abbb.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.942052583391923  
**Tags**: "plate" "food" "table" "indoor" "sashimi" "sitting" "wooden" "filled" "top" "full" "bowl" "holding" "black" "meat" "fruit" "cake" "hot" "large" "red" "white" "salad"

* * *

![](http://cdn.sotong.io/insta/9cc9858dcbe77f5aef916f1bdcac3682.jpg)  
**Text:** "a city street filled with traffic at night"  
**Confidence**: 0.9392489244865508  
**Tags**: "building" "outdoor" "street" "road" "city" "light" "traffic" "busy" "night" "lit" "filled" "many" "sign" "driving" "people" "bunch" "pedestrians" "walking" "large" "intersection" "tall" "riding" "bus" "woman" "standing" "man"

* * *

![](http://cdn.sotong.io/insta/2528d9e40f6ed93cba455042f81b1963.jpg)  
**Text:** "a table full of food sitting on a plate"  
**Confidence**: 0.9364228594426324  
**Tags**: "plate" "table" "food" "indoor" "sitting" "dining" "dinner" "full" "top" "filled" "topped" "bowl" "restaurant" "many" "meal" "different" "eating" "set" "several" "woman" "people" "counter" "glasses" "group" "holding" "room" "wooden" "large" "wine" "meat" "white" "water" "standing"

* * *

![](http://cdn.sotong.io/insta/b7433d12f91de4a37aff5b685003a65a.jpg)  
**Text:** "a view of a snow covered mountain"  
**Confidence**: 0.933540174987247  
**Tags**: "outdoor" "snow" "nature" "plane" "view" "mountain" "window" "airplane" "top" "covered" "flying" "clouds" "skiing" "hill" "high" "seen" "sun" "side" "air" "water" "slope" "standing" "group" "people"

* * *

![](http://cdn.sotong.io/insta/c34ae6eb737912845ed4a26b9b8f8b40.jpg)  
**Text:** "a group of people walking in front of a building"  
**Confidence**: 0.930803588432749  
**Tags**: "building" "outdoor" "people" "clock" "group" "walking" "standing" "front" "city" "tower" "street" "water" "top" "large" "crowd" "brick" "man" "beach" "road" "red" "kite" "tall"

* * *

![](http://cdn.sotong.io/insta/9e2e74b69f0ab6ae8928b17c2616b6ea.jpg)  
**Text:** "a group of people walking down a street"  
**Confidence**: 0.9297631272152411  
**Tags**: "outdoor" "building" "person" "street" "people" "walking" "road" "group" "city" "standing" "woman" "sidewalk" "man" "riding" "holding" "traffic" "crowd" "train"

* * *

![](http://cdn.sotong.io/insta/e37d6a632722cf3abd01180118d7c7c1.jpg)  
**Text:** "a crowded city street filled with traffic at night"  
**Confidence**: 0.9260563138933241  
**Tags**: "light" "outdoor" "street" "night" "fireworks" "traffic" "dark" "lit" "city" "building" "car" "busy" "view" "driving" "people" "filled" "intersection" "sign" "group" "bunch" "standing" "stop" "snow" "signal" "crowded" "crowd" "blurry" "man" "hydrant" "riding" "bus"

* * *

![](http://cdn.sotong.io/insta/532daed5dda10d5159815f793e8483fb.jpg)  
**Text:** "a close up of a pizza"  
**Confidence**: 0.9246481371443355  
**Tags**: "pizza" "food" "table" "sitting" "cheese" "plate" "top" "piece" "slice" "toppings" "close" "eaten" "sauce" "covered" "wooden" "large" "pepperoni" "white" "pan"

* * *

![](http://cdn.sotong.io/insta/5eb3d20ada4f492ebf9c7526142fd63f.jpg)  
**Text:** "there are many different plates of food on a table"  
**Confidence**: 0.9228319348150278  
**Tags**: "plate" "food" "table" "different" "filled" "many" "meat" "full" "several" "various" "bowl" "holding" "topped" "small" "items" "set" "sitting" "brown" "rice" "dinner" "assorted" "counter" "wooden" "bunch" "group" "white" "laying"

* * *

![](http://cdn.sotong.io/insta/eb96b83a1ba66c59b3cfee259d9af6a3.jpg)  
**Text:** "a close up of a sandwich on a plate on a table"  
**Confidence**: 0.9112371332777958  
**Tags**: "table" "cup" "food" "plate" "sandwich" "sitting" "coffee" "glass" "top" "filled" "white" "close" "large" "half" "tall" "cut" "cake"

* * *

![](http://cdn.sotong.io/insta/fc153040de0d248492774afbeff92666.jpg)  
**Text:** "a table with many plates of food"  
**Confidence**: 0.9099985667476314  
**Tags**: "plate" "food" "table" "sitting" "bowl" "counter" "top" "filled" "different" "many" "small" "front" "holding" "topped" "several" "various" "meat" "large" "brown" "woman" "rice" "white" "group" "people" "room" "soup"

* * *

![](http://cdn.sotong.io/insta/b7f47d973f42b4ef12dba185ce604840.jpg)  
**Text:** "a living room filled with furniture and a large window"  
**Confidence**: 0.9078564235094314  
**Tags**: "indoor" "room" "table" "window" "living" "chair" "furniture" "large" "building" "area" "filled" "white" "decorated" "glass" "place" "sitting" "television" "dining" "fireplace" "hotel" "view" "several" "plate" "bed" "bedroom" "fire"

* * *

![](http://cdn.sotong.io/insta/b1e0e8873c718b23bf4095eb048980f6.jpg)  
**Text:** "a small boat in a body of water"  
**Confidence**: 0.9070077510141389  
**Tags**: "water" "outdoor" "boat" "small" "riding" "harbor" "river" "man" "lake" "floating" "colorful" "large" "people" "traveling" "sitting" "body" "top" "little" "yellow" "ocean" "group" "blue" "standing" "city" "red" "docked"

* * *

![](http://cdn.sotong.io/insta/85ec34bfd66b2967227d9308b2f6c52f.jpg)  
**Text:** "a living room filled with furniture next to a book shelf"  
**Confidence**: 0.906123715522115  
**Tags**: "indoor" "room" "living" "table" "shelf" "book" "red" "chair" "sitting" "furniture" "desk" "filled" "area" "small" "office" "computer" "laptop" "fire" "black" "fireplace" "large" "dog" "library" "bedroom" "pink" "bed" "white"

* * *

![](http://cdn.sotong.io/insta/6a23c3b6f95e395e216c3dd4c24c16e4.jpg)  
**Text:** "a slice of cake and a cup of coffee"  
**Confidence**: 0.9053528163240419  
**Tags**: "cup" "table" "coffee" "cake" "food" "sitting" "indoor" "piece" "slice" "chocolate" "plate" "dessert" "cream" "ice" "top" "fruit" "banana" "glass" "fork" "close" "orange" "cut" "sandwich" "phone" "white"

* * *

![](http://cdn.sotong.io/insta/06418cbdcd6f951495e47c8b3cf04560.jpg)  
**Text:** "a piece of cake on a paper plate"  
**Confidence**: 0.901666132328936  
**Tags**: "piece" "food" "cake" "plate" "slice" "sitting" "eaten" "paper" "white" "fork" "dessert" "half" "top" "close" "small" "table" "cheese"

* * *

![](http://cdn.sotong.io/insta/39ba16db41c53641625e215a25b138d7.jpg)  
**Text:** "a plate of food and fruit"  
**Confidence**: 0.899701452713716  
**Tags**: "food" "table" "plate" "fruit" "slice" "piece" "cake" "sitting" "small" "fork" "dessert" "banana" "sliced" "top" "bowl" "cheese" "cutting" "meat" "cut" "laying" "holding" "white"

* * *

![](http://cdn.sotong.io/insta/4e9d82d1b31712cd81db6009ef154681.jpg)  
**Text:** "a hotel room with a large bed in a bedroom"  
**Confidence**: 0.8931900965791019  
**Tags**: "floor" "indoor" "bed" "window" "bedroom" "hotel" "room" "table" "large" "sitting" "made" "big" "wooden" "night" "desk" "side" "white" "standing" "double" "board"

* * *

![](http://cdn.sotong.io/insta/d6fe1b505d21e65740f2651b2d609d43.jpg)  
**Text:** "a crowded city street filled with traffic at night"  
**Confidence**: 0.892763989975461  
**Tags**: "building" "outdoor" "street" "city" "traffic" "car" "filled" "light" "busy" "going" "river" "boat" "water" "night" "large" "driving" "crowded" "view" "riding" "standing" "people" "colorful" "harbor" "man" "group" "rain" "umbrella" "sign" "crowd" "road"

* * *

![](http://cdn.sotong.io/insta/ce61bf721c8e129c6e2e7110e10fc9c4.jpg)  
**Text:** "a car parked in front of a building"  
**Confidence**: 0.8927145688595874  
**Tags**: "building" "outdoor" "road" "car" "street" "city" "parked" "front" "sitting" "red" "sign" "driving" "side" "people" "standing" "large" "snow" "white" "busy" "riding" "bus" "group" "man" "traffic" "tall"

* * *

![](http://cdn.sotong.io/insta/79c8d06c2e93ee67d570f865b5550ebf.jpg)  
**Text:** "a sandy beach next to a palm tree"  
**Confidence**: 0.8915600626434229  
**Tags**: "outdoor" "beach" "water" "palm" "tree" "ocean" "plant" "sandy" "body" "shade" "grass" "sitting" "cow" "lined" "empty" "laying" "front" "sand" "shore" "herd" "umbrella" "standing" "boat" "bench" "large" "lake" "people" "surfing" "walking" "flying" "sun" "group" "board" "giraffe" "wave" "sunset" "swimming" "white" "man"

* * *

![](http://cdn.sotong.io/insta/ed256e3062d5207988288bdd888e3965.jpg)  
**Text:** "a cup of coffee"  
**Confidence**: 0.8904119310458819  
**Tags**: "cup" "coffee" "table" "indoor" "sitting" "window" "food" "breakfast" "donut" "doughnut" "computer" "laptop" "glass" "desk" "keyboard" "white" "sandwich" "phone" "plate"

* * *

![](http://cdn.sotong.io/insta/34db0e76e501ddee651aa2b406628c24.jpg)  
**Text:** "a group of people walking in front of a building"  
**Confidence**: 0.8903561448018456  
**Tags**: "building" "outdoor" "person" "people" "group" "street" "walking" "standing" "city" "front" "man" "elephant" "riding" "large" "bus" "table" "crowd" "store" "holding" "umbrella" "parked" "road" "sign"

* * *

![](http://cdn.sotong.io/insta/7596aa2975f6b4b0044f24a97d714637.jpg)  
**Text:** "a slice of pizza"  
**Confidence**: 0.8890888465473035  
**Tags**: "food" "pizza" "indoor" "slice" "piece" "table" "sitting" "wooden" "cut" "top" "box" "plate" "cheese" "cutting" "covered" "pan" "board"

* * *

![](http://cdn.sotong.io/insta/47e01376d4aaedf29816b5f17818ea55.jpg)  
**Text:** "a close up of a plate of food on a table"  
**Confidence**: 0.8835956123013228  
**Tags**: "food" "table" "cup" "sitting" "plate" "piece" "slice" "top" "paper" "cake" "topped" "white" "cut" "close" "half" "green" "sandwich" "glass" "fruit" "fries"

* * *

![](http://cdn.sotong.io/insta/8eb03fa967a8e0468e10218a6c0bbb30.jpg)  
**Text:** "a sign in front of a building"  
**Confidence**: 0.8828267075282481  
**Tags**: "building" "outdoor" "sign" "street" "red" "sitting" "front" "city" "side" "large" "top" "pole" "stop" "woman" "white" "tall" "standing"

* * *

![](http://cdn.sotong.io/insta/2b7774714f7bdb11fb3b152c9eb114dd.jpg)  
**Text:** "a pizza with cheese and pepperoni"  
**Confidence**: 0.880928192880279  
**Tags**: "pizza" "food" "pepperoni" "sitting" "small" "cheese" "indoor" "top" "slice" "black" "plate" "white" "table" "tray" "fresh" "baked" "wooden" "large" "close" "pan"

* * *

![](http://cdn.sotong.io/insta/edbf5ba7daa05ea97898056610e1f068.jpg)  
**Text:** "a bowl filled with pasta and broccoli"  
**Confidence**: 0.8806435727800993  
**Tags**: "food" "plate" "vegetable" "table" "bowl" "broccoli" "dish" "pasta" "filled" "sauce" "white" "meat" "meal" "rice" "dinner" "full" "sitting" "fork" "cheese" "cooked" "salad"

* * *

![](http://cdn.sotong.io/insta/3ce1fdc664f4966c9f47e9ba95201ab7.jpg)  
**Text:** "a bowl of soup"  
**Confidence**: 0.8778186645810226  
**Tags**: "food" "plate" "bowl" "table" "soup" "sitting" "cup" "filled" "small" "top" "white" "cake" "brown" "sauce" "stew" "sandwich" "cheese"

* * *

![](http://cdn.sotong.io/insta/574d36e5f68287061e2bd20a0e794fe2.jpg)  
**Text:** "a group of people standing in front of a crowd"  
**Confidence**: 0.8777132753249887  
**Tags**: "person" "building" "crowd" "people" "large" "train" "group" "standing" "front" "stadium" "man" "crowded" "red" "auditorium" "waiting" "wearing" "many" "station" "track" "holding" "yellow" "elephant" "white"

* * *

![](http://cdn.sotong.io/insta/008fcaec2e7001c50f28728db4a3304b.jpg)  
**Text:** "a group of people standing in front of a store"  
**Confidence**: 0.8765926059566164  
**Tags**: "building" "outdoor" "people" "person" "group" "train" "standing" "store" "street" "walking" "front" "line" "waiting" "man" "station" "sign" "city" "platform" "night" "large" "woman" "busy" "bus" "subway" "room"

* * *

![](http://cdn.sotong.io/insta/c4f26e86435996c8d961938b06a50208.jpg)  
**Text:** "a bowl of soup"  
**Confidence**: 0.8761553494917715  
**Tags**: "food" "bowl" "table" "indoor" "plate" "soup" "sitting" "spoon" "filled" "top" "different" "stew" "brown" "wooden" "holding" "meat" "rice"

* * *

![](http://cdn.sotong.io/insta/9bf41078e9616fb75558e41cc6ac4974.jpg)  
**Text:** "a view of a city street filled with traffic at night"  
**Confidence**: 0.8718691966142273  
**Tags**: "outdoor" "light" "water" "night" "street" "city" "view" "traffic" "lit" "filled" "tree" "lot" "busy" "lake" "river" "body" "driving" "boat" "red" "group" "sign"

* * *

![](http://cdn.sotong.io/insta/20cef5964bb702e24e70ce0b1be12fa9.jpg)  
**Text:** "a dish of meat and vegetables"  
**Confidence**: 0.8717755196439632  
**Tags**: "food" "plate" "table" "dish" "meat" "bowl" "sitting" "filled" "small" "top" "different" "brown" "sauce" "white" "holding" "broccoli"

* * *

![](http://cdn.sotong.io/insta/7472c72c28263994836b20cfda996bd3.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.8714357579904919  
**Tags**: "plate" "food" "table" "sashimi" "indoor" "bowl" "small" "filled" "sitting" "meat" "black" "top" "different" "pink" "cake" "holding" "fruit" "red" "salad" "laying"

* * *

![](http://cdn.sotong.io/insta/0ca7dee95870b5076078896b87e704b5.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.8705157832367294  
**Tags**: "food" "indoor" "table" "plate" "sitting" "top" "filled" "topped" "black" "meat" "cheese" "bowl" "fruit" "hot" "cake" "white"

* * *

![](http://cdn.sotong.io/insta/658a4af77440fcc108588a4ce3af0159.jpg)  
**Text:** "a group of people walking in front of a crowd"  
**Confidence**: 0.8693071244954825  
**Tags**: "person" "outdoor" "building" "people" "sport" "road" "group" "street" "child" "standing" "crowd" "walking" "front" "young" "small" "man" "boy" "sidewalk" "holding" "city" "woman" "large" "lot" "playing" "riding" "train" "board" "trick" "elephant" "ball"

* * *

![](http://cdn.sotong.io/insta/602cadf518e29a8ebd8b583258c7c376.jpg)  
**Text:** "a close up of a plate of food with meat and vegetables"  
**Confidence**: 0.8692373029033967  
**Tags**: "food" "plate" "sandwich" "top" "white" "meat" "bun" "dish" "table" "paper" "sauce" "sitting" "meal" "small" "fries" "close" "pile" "chicken" "large" "covered" "lettuce" "eating" "holding" "salad"

* * *

![](http://cdn.sotong.io/insta/3393b76bd7b5fac5ff1eaa753159cc26.jpg)  
**Text:** "a piece of cake on a plate"  
**Confidence**: 0.8690471160546493  
**Tags**: "food" "piece" "plate" "cake" "slice" "doughnut" "donut" "table" "eaten" "cream" "fruit" "half" "dessert" "paper" "small" "snow" "top" "sitting" "banana" "orange" "covered" "topped" "filled" "sauce" "white" "meat" "cut" "laying" "holding" "oranges"

* * *

![](http://cdn.sotong.io/insta/a10067c00ec1e58270ae06edf37a4cd7.jpg)  
**Text:** "a crowd of people walking on a city street"  
**Confidence**: 0.8680606443754513  
**Tags**: "building" "outdoor" "people" "person" "road" "street" "walking" "clock" "city" "sidewalk" "standing" "group" "crowd" "busy" "train" "store" "man" "large" "woman" "holding" "station" "restaurant" "crowded" "tower" "white" "tall" "parked"

* * *

![](http://cdn.sotong.io/insta/81f077073c6290fdf723734635189e29.jpg)  
**Text:** "a small boat in a large body of water"  
**Confidence**: 0.86340733845801  
**Tags**: "water" "outdoor" "mountain" "lake" "river" "boat" "body" "background" "pond" "train" "large" "surrounded" "small" "traveling" "red" "middle" "floating" "forest" "green" "bridge"

* * *

![](http://cdn.sotong.io/insta/61bd31bf585c942775ebf5971ed35bc3.jpg)  
**Text:** "a living room filled with furniture and decor"  
**Confidence**: 0.8624918386084086  
**Tags**: "indoor" "room" "living" "table" "chair" "furniture" "window" "filled" "building" "area" "decorated" "sitting" "large" "blue"

* * *

![](http://cdn.sotong.io/insta/bf0910cc47b442d8f629d048cd07fd9e.jpg)  
**Text:** "a city street filled with traffic at night"  
**Confidence**: 0.8621638198227449  
**Tags**: "building" "outdoor" "street" "road" "city" "car" "busy" "walking" "filled" "sidewalk" "people" "train" "side" "night" "traffic" "driving" "large" "woman" "standing" "riding" "tall" "track" "parked" "group" "man"

* * *

![](http://cdn.sotong.io/insta/55e099062d16f621ce89d24fcd01996d.jpg)  
**Text:** "a sunset at the beach"  
**Confidence**: 0.8592678001801027  
**Tags**: "outdoor" "beach" "sunset" "water" "sun" "nature" "ocean" "man" "surfing" "top" "sand" "sandy" "track" "walking" "standing" "board" "riding" "flying" "people" "wave"

* * *

![](http://cdn.sotong.io/insta/7d7ad598d95231bcb49e3e004abe1e74.jpg)  
**Text:** "a slice of cake on a plate"  
**Confidence**: 0.8562800872016758  
**Tags**: "plate" "food" "cake" "table" "piece" "cup" "dessert" "slice" "sitting" "coffee" "top" "small" "fruit" "chocolate" "fork" "cream" "banana" "white" "orange" "sauce" "snow" "covered"

* * *

![](http://cdn.sotong.io/insta/5b003145482955a21a05ec1ddec2d43c.jpg)  
**Text:** "a plate of food that includes pizza and a salad"  
**Confidence**: 0.8548645133485088  
**Tags**: "food" "table" "wooden" "sitting" "plate" "top" "pizza" "sandwich" "topped" "cutting" "salad" "covered" "meat" "toppings" "eating" "cheese" "white" "board" "lettuce"

* * *

![](http://cdn.sotong.io/insta/9fbf75d11bb5d1abd3cf6e6260286c28.jpg)  
**Text:** "a cup of coffee"  
**Confidence**: 0.8527612488821656  
**Tags**: "cup" "table" "coffee" "food" "sitting" "drink" "plate" "sandwich" "breakfast" "spoon" "glass" "close" "donut" "hot" "white" "phone" "soup"

* * *

![](http://cdn.sotong.io/insta/fab2b56d80e73a8bd468400abc3e5006.jpg)  
**Text:** "a small boat in a large body of water"  
**Confidence**: 0.8492568828886582  
**Tags**: "water" "outdoor" "boat" "nature" "ocean" "lake" "small" "body" "floating" "large" "surrounded" "top" "river" "green" "pond" "clear" "many" "blue" "flock" "beach" "city" "people" "group" "umbrella"

* * *

![](http://cdn.sotong.io/insta/3224096f55ad5eb18da04e1d11c5240a.jpg)  
**Text:** "a living room filled with furniture and a large window"  
**Confidence**: 0.8483319091737124  
**Tags**: "indoor" "table" "room" "living" "chair" "filled" "window" "furniture" "sitting" "glass" "area" "library" "large" "wooden" "television" "desk" "white" "bed" "bedroom"

* * *

![](http://cdn.sotong.io/insta/c14293c28c50cb973a5e7a9be88f532f.jpg)  
**Text:** "a plate of food with meat and vegetables"  
**Confidence**: 0.8479946508543239  
**Tags**: "food" "plate" "table" "indoor" "sitting" "small" "tray" "white" "filled" "red" "cut" "meat" "sandwich"

* * *

![](http://cdn.sotong.io/insta/cddf90e97c0ed3940d394542d838ea53.jpg)  
**Text:** "a group of people on a beach"  
**Confidence**: 0.8472987058060032  
**Tags**: "outdoor" "beach" "water" "nature" "people" "ocean" "flying" "day" "top" "sandy" "group" "cloudy" "standing" "large" "kite" "man" "umbrella" "blue" "wave"

* * *

![](http://cdn.sotong.io/insta/a4496de6824ec6e0ff991b63adbd2f10.jpg)  
**Text:** "a crowded city street filled with traffic at night"  
**Confidence**: 0.8466275472706768  
**Tags**: "building" "city" "many" "night" "filled" "street" "bunch" "colorful" "people" "walking" "large" "sign" "lit" "busy" "crowd" "lot" "light" "group" "standing" "crowded" "traffic" "tall"

* * *

![](http://cdn.sotong.io/insta/9d4d37a39292d2ff6c5a6e51007fb4af.jpg)  
**Text:** "a bottle of beer"  
**Confidence**: 0.8438430778285878  
**Tags**: "bottle" "table" "indoor" "beer" "sitting" "food" "wine" "top" "pizza" "sandwich" "counter" "computer" "kitchen" "empty" "wooden" "green" "cutting" "close" "bar" "refrigerator" "keyboard" "desk" "plate" "meat" "white" "standing" "eating" "water" "laying"

* * *

![](http://cdn.sotong.io/insta/6f77bf47f23c711a822139da57890261.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.8435932250366942  
**Tags**: "food" "plate" "table" "indoor" "sitting" "egg" "tray" "sauce" "small" "meal" "sandwich" "eaten" "top" "meat" "white" "fork" "cake" "bowl" "holding" "hot" "cheese" "soup"

* * *

![](http://cdn.sotong.io/insta/7a032cd1e936e188d9a3efe261a7b93c.jpg)  
**Text:** "a view of a tall building"  
**Confidence**: 0.843138107425618  
**Tags**: "outdoor" "building" "city" "tall" "bridge" "skyscraper" "large" "view" "boat" "top" "tower" "side" "water" "man" "standing" "street" "bus" "air" "white"

* * *

![](http://cdn.sotong.io/insta/6a8e4f9473bb6863324e6d6d86d6f6cc.jpg)  
**Text:** "a large ship in the background"  
**Confidence**: 0.8430498016150385  
**Tags**: "boat" "ship" "watercraft" "outdoor" "large" "water" "transport" "dock" "docked" "big" "white" "sitting" "top" "bird" "man" "group" "people" "dog" "floating" "standing" "ocean" "city" "plane"

* * *

![](http://cdn.sotong.io/insta/4a9e92d585f8928e05eb9b8b4faada1f.jpg)  
**Text:** "a dining room table"  
**Confidence**: 0.8425506799745854  
**Tags**: "table" "indoor" "red" "sitting" "window" "top" "counter" "dining" "area" "food" "glass" "wooden" "wine" "large" "orange" "room" "kitchen" "restaurant" "plate" "standing" "woman" "people" "man"

* * *

![](http://cdn.sotong.io/insta/3e62f168ada2e4924aebed4863b29b5e.jpg)  
**Text:** "a group of people posing for a picture"  
**Confidence**: 0.8425331728390407  
**Tags**: "person" "outdoor" "standing" "group" "people" "posing" "photo" "woman" "young" "wearing" "holding" "child" "girl" "snow" "man" "skiing" "city" "street" "white" "field"

* * *

![](http://cdn.sotong.io/insta/4a1b1bbcc8450573f064e023de0e63e1.jpg)  
**Text:** "a group of people standing in front of a crowd"  
**Confidence**: 0.8406140866647169  
**Tags**: "person" "outdoor" "people" "building" "group" "standing" "walking" "street" "crowd" "holding" "man" "woman" "bus" "large" "city" "red" "white" "crowded"

* * *

![](http://cdn.sotong.io/insta/7537acdb6ea57474dfe175beebe9fda3.jpg)  
**Text:** "a view of a mountain"  
**Confidence**: 0.8391738784950346  
**Tags**: "outdoor" "grass" "mountain" "view" "large" "city" "sitting" "overlooking" "hill" "green" "field" "grassy" "park" "standing" "flying" "street" "sign" "people" "water" "man" "river"

* * *

![](http://cdn.sotong.io/insta/226efef98770bbfd0d81a17516568413.jpg)  
**Text:** "a view of a body of water"  
**Confidence**: 0.8382113880892157  
**Tags**: "water" "outdoor" "river" "boat" "body" "sunset" "sitting" "lake" "large" "tree" "many" "sun" "view" "several" "group" "night" "red"

* * *

![](http://cdn.sotong.io/insta/5a4ee3e4e1326c510519cfeae9a8ebf3.jpg)  
**Text:** "a large tree"  
**Confidence**: 0.8379659851717577  
**Tags**: "outdoor" "tree" "sitting" "palm" "water" "park" "top" "branch" "large" "green" "lake" "tower" "bench" "tall" "perched" "red" "standing" "bird" "field" "street" "clock" "white" "sign" "man" "group"

* * *

![](http://cdn.sotong.io/insta/870f8c1e10771cdfce8135120ed9d9c5.jpg)  
**Text:** "a palm tree"  
**Confidence**: 0.8377333847627662  
**Tags**: "outdoor" "plant" "tree" "palm" "beach" "water" "large" "front" "flying" "clock" "kite" "ocean" "standing" "man" "blue" "red" "grazing" "walking" "tall" "green" "board" "air" "street" "tower" "surfing" "yellow" "riding" "group" "umbrella" "field" "white" "herd" "people"

* * *

![](http://cdn.sotong.io/insta/38d4824a92f17d3e664ede1c1db1f5c5.jpg)  
**Text:** "a tree sitting in the middle of a forest"  
**Confidence**: 0.837195745141177  
**Tags**: "plant" "tree" "forest" "outdoor" "grass" "green" "wood" "park" "bench" "sitting" "area" "path" "dirt" "middle" "standing" "wooden" "black" "hydrant" "white" "fire" "large" "red" "field" "sign"

* * *

![](http://cdn.sotong.io/insta/efe43152274e9fce7e93dc78181340c3.jpg)  
**Text:** "a wooden table next to a window"  
**Confidence**: 0.8365439206950018  
**Tags**: "table" "indoor" "window" "room" "sitting" "chair" "small" "desk" "wooden" "laptop" "lit" "top" "light" "counter" "computer" "living" "kitchen"

* * *

![](http://cdn.sotong.io/insta/087416fdbd6fd64c107e61523464c37d.jpg)  
**Text:** "several different types of cake"  
**Confidence**: 0.8361765221820519  
**Tags**: "cake" "table" "indoor" "food" "plate" "display" "red" "filled" "bunch" "different" "several" "top" "birthday" "party" "dessert" "sitting" "displayed" "large" "fruit" "sign"

* * *

![](http://cdn.sotong.io/insta/4562eedfd1fdf62d9858ca24e69666d7.jpg)  
**Text:** "a sunset over a body of water"  
**Confidence**: 0.8334563990737236  
**Tags**: "outdoor" "water" "sunset" "sun" "river" "body" "background" "boat" "going" "lake" "view" "large" "clouds" "traveling" "mountain" "ocean" "tree" "track" "train" "city"

* * *

![](http://cdn.sotong.io/insta/cf951eed623c30a926e63762da3fc0ce.jpg)  
**Text:** "a sign on the side of a building"  
**Confidence**: 0.8317563977063288  
**Tags**: "outdoor" "sign" "building" "street" "stop" "standing" "city" "front" "side" "large" "brick" "tall" "red" "clock"

* * *

![](http://cdn.sotong.io/insta/2cd1dcb0a9c967012775b36445b7be8b.jpg)  
**Text:** "a cheese pizza on a pan"  
**Confidence**: 0.8288403013213312  
**Tags**: "pizza" "food" "pan" "sitting" "table" "cheese" "metal" "large" "top" "tray" "holding" "baked" "plate" "wooden" "oven" "sauce" "pasta" "black" "bowl" "cooking" "player" "white" "stove"

* * *

![](http://cdn.sotong.io/insta/53fca2d0e4cf559b901add492e066b02.jpg)  
**Text:** "a view of a boat"  
**Confidence**: 0.824378336551607  
**Tags**: "outdoor" "boat" "water" "view" "city" "light" "lake" "large" "train" "side" "hanging" "hill" "street" "traffic" "track" "group" "white"

* * *

![](http://cdn.sotong.io/insta/4e7021e3f688387ccc1ff6dd1f439d41.jpg)  
**Text:** "a group of people standing around a table with food"  
**Confidence**: 0.824187206439623  
**Tags**: "person" "indoor" "table" "man" "food" "counter" "people" "standing" "sitting" "front" "looking" "plate" "woman" "desk" "preparing" "group" "cake" "bowl" "kitchen" "holding" "computer" "room"

* * *

![](http://cdn.sotong.io/insta/1e5ec45ec65d8e75d29d94c46c6a77ab.jpg)  
**Text:** "a group of people standing in front of a bar"  
**Confidence**: 0.8206947607038934  
**Tags**: "person" "indoor" "table" "ceiling" "people" "man" "group" "standing" "wine" "food" "room" "kitchen" "bar" "glasses" "woman" "restaurant" "front" "drinking" "preparing" "large" "living" "counter" "cooking" "holding" "crowd"

* * *

![](http://cdn.sotong.io/insta/2dc4df496aa460a19c5025b5daf9658e.jpg)  
**Text:** "a group of people walking down a street next to tall buildings"  
**Confidence**: 0.8203631150085597  
**Tags**: "building" "outdoor" "street" "scene" "walking" "people" "person" "city" "sidewalk" "road" "town" "standing" "group" "narrow" "crowd" "pedestrians" "sign" "woman" "side" "brick" "parked" "riding" "tall" "old" "holding" "large" "busy" "stop" "motorcycle" "man" "umbrella"

* * *

![](http://cdn.sotong.io/insta/ddc315d41c3edb3ab790b5341b41558b.jpg)  
**Text:** "a plate that has some fruit on a table"  
**Confidence**: 0.8169438145249394  
**Tags**: "plate" "food" "table" "fruit" "sitting" "top" "dessert" "slice" "wooden" "cake" "cream" "small" "topped" "piece" "bowl" "banana" "white" "cheese" "orange" "pizza" "fork" "black" "meat" "covered" "oranges"

* * *

![](http://cdn.sotong.io/insta/01439a266efdbfde6de2cf1be3ec9f94.jpg)  
**Text:** "a bottle of wine"  
**Confidence**: 0.8157202493512721  
**Tags**: "bottle" "indoor" "wine" "food" "table" "sitting" "filled" "counter" "top" "wooden" "kitchen" "glass" "refrigerator" "pizza"

* * *

![](http://cdn.sotong.io/insta/e98347aab1484f46e5b5bf31a35143d9.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.8152296805878695  
**Tags**: "plate" "food" "table" "sitting" "small" "bowl" "top" "filled" "meat" "fruit" "white"

* * *

![](http://cdn.sotong.io/insta/3a80c04adb63d4520ea7f79cf5f46625.jpg)  
**Text:** "a plate of food and a cup of coffee"  
**Confidence**: 0.814853102434509  
**Tags**: "food" "cup" "table" "coffee" "plate" "breakfast" "sitting" "filled" "black" "meal" "bowl" "wooden" "hot" "rice" "fruit" "holding" "keyboard" "cake" "glass" "meat" "sandwich" "cheese" "phone"

* * *

![](http://cdn.sotong.io/insta/2688dc507c8ba2bda71a8d101f613c88.jpg)  
**Text:** "a hotel room with a bed and a large window"  
**Confidence**: 0.8144870995788417  
**Tags**: "indoor" "ceiling" "hotel" "room" "window" "bed" "bedroom" "table" "large" "nice" "living" "chair" "flat" "building" "furniture" "looking" "sitting" "view" "lamp" "made" "water" "decorated" "television" "area" "glass" "clean" "screen" "wooden" "double" "white" "ocean"

* * *

![](http://cdn.sotong.io/insta/fc471b4facc33aac324ce1207a5c788d.jpg)  
**Text:** "a group of people on a beach"  
**Confidence**: 0.8137470468464388  
**Tags**: "outdoor" "water" "beach" "nature" "people" "man" "group" "sitting" "standing" "playing" "young" "tree" "boy" "flying" "several" "walking" "large" "riding" "palm" "kite" "air"

* * *

![](http://cdn.sotong.io/insta/4fbf3dfa13c7b919d6742443f9fdc45f.jpg)  
**Text:** "a group of people walking down a street next to tall buildings"  
**Confidence**: 0.811666530518435  
**Tags**: "outdoor" "building" "people" "street" "walking" "standing" "group" "city" "sidewalk" "front" "road" "large" "top" "clock" "man" "tall" "old" "many" "crowd" "table" "woman" "parked" "tower" "riding" "snow"

* * *

![](http://cdn.sotong.io/insta/b1ff33dbbb9d87942654031ee388721e.jpg)  
**Text:** "a view of a city skyline in the background"  
**Confidence**: 0.8088881427215502  
**Tags**: "outdoor" "city" "mountain" "building" "large" "background" "water" "view" "harbor" "hill" "boat" "top" "flying" "river" "body" "plane" "airplane" "snow" "tall" "ocean" "air" "traffic" "skiing" "white" "people" "slope" "street"

* * *

![](http://cdn.sotong.io/insta/2a5dfc7f9f8622f4f125cbc386f5e263.jpg)  
**Text:** "a plate of food and a cup of coffee"  
**Confidence**: 0.8068681636633935  
**Tags**: "food" "table" "cup" "plate" "coffee" "sitting" "topped" "black" "top" "fruit" "filled" "glass" "chocolate" "hot" "white"

* * *

![](http://cdn.sotong.io/insta/19de02f4fe51aeb33f73132796f0b582.jpg)  
**Text:** "a sunset over the ocean"  
**Confidence**: 0.8065587199349568  
**Tags**: "outdoor" "water" "beach" "sunset" "ocean" "sun" "man" "pier" "track" "board" "top" "large" "red" "standing" "surfing" "walking" "boat" "holding" "flying" "yellow" "sand" "riding" "wave" "people"

* * *

![](http://cdn.sotong.io/insta/5bfdef8f0af968ddc352e88f30fe0bfd.jpg)  
**Text:** "a group of people on a beach with palm trees"  
**Confidence**: 0.8047401902111697  
**Tags**: "outdoor" "beach" "water" "tree" "palm" "people" "sandy" "group" "ocean" "riding" "flying" "sand" "body" "large" "walking" "umbrella" "surfing" "kite" "herd" "man"

* * *

![](http://cdn.sotong.io/insta/f8f23cbab7de4ed1d9e2b353fb4ddc8a.jpg)  
**Text:** "a piece of pizza on a plate"  
**Confidence**: 0.8024798319484584  
**Tags**: "food" "plate" "piece" "slice" "sitting" "table" "sauce" "white" "paper" "top" "small" "bread" "red" "cheese" "meat" "covered" "pizza" "bun" "sandwich" "laying"

* * *

![](http://cdn.sotong.io/insta/05b2596a77647c8684c7ed639dcbf0db.jpg)  
**Text:** "a group of people walking in front of a church"  
**Confidence**: 0.8012557784636437  
**Tags**: "outdoor" "building" "people" "church" "walking" "front" "group" "large" "old" "street" "stone" "man" "square" "woman" "cross" "park" "top" "standing" "riding" "city" "statue" "tower" "snow" "clock" "horse" "carriage" "white" "tall" "crowd" "parked"

* * *

![](http://cdn.sotong.io/insta/7d189bdbee2f7b34cd447745afa23d6a.jpg)  
**Text:** "a view of a mountain"  
**Confidence**: 0.7998601465351945  
**Tags**: "mountain" "outdoor" "hill" "flying" "background" "large" "clouds" "top" "water" "view" "cloudy" "hillside" "standing" "tree" "ocean" "dark" "day" "green" "grassy" "high" "air" "kite" "field" "airplane" "bird" "man" "grazing" "plane" "sunset" "group" "blue" "tall" "river"

* * *

![](http://cdn.sotong.io/insta/8c13e99bed16cee9a761b31df86bbc53.jpg)  
**Text:** "a view of a city"  
**Confidence**: 0.7996958049267279  
**Tags**: "outdoor" "building" "city" "green" "view" "mountain" "background" "sitting" "large" "day" "water" "traffic" "street" "light" "top" "many" "park" "cloudy" "river" "tall" "tower" "field"

* * *

![](http://cdn.sotong.io/insta/0e047ba58801cc9df3b5e493d8f91b9d.jpg)  
**Text:** "a close up of a plate of pizza topped with cheese and tomatoes"  
**Confidence**: 0.7987180036355725  
**Tags**: "food" "plate" "tomato" "sauce" "top" "pizza" "topped" "cheese" "piece" "pepperoni" "slice" "table" "white" "fruit" "small" "sitting" "fresh" "meat" "red" "laying" "close" "hot" "covered" "green"

* * *

![](http://cdn.sotong.io/insta/af80c67d26a1cc027b0185eebbe9038f.jpg)  
**Text:** "a tray filled with different types of food on a table"  
**Confidence**: 0.798385211420478  
**Tags**: "food" "table" "plate" "tray" "fruit" "sitting" "dog" "filled" "hot" "different" "meat" "various" "bowl" "cheese" "covered" "holding"

* * *

![](http://cdn.sotong.io/insta/42d14d450e24e9ed47ee0a0e9bb40470.jpg)  
**Text:** "a plate of food on a table"  
**Confidence**: 0.7966582500450602  
**Tags**: "food" "plate" "table" "indoor" "sitting" "meat" "sandwich" "small" "top" "bowl" "filled" "different" "white" "black" "salad"

* * *

![](http://cdn.sotong.io/insta/5b7b79314998e85bc2451cd398543873.jpg)  
**Text:** "a large building"  
**Confidence**: 0.7964848923559359  
**Tags**: "building" "outdoor" "large" "front" "sitting" "white" "street" "city" "top" "parked" "water" "walking" "old" "tall" "driving" "boat" "bench" "man" "riding" "red" "window" "clock" "sign" "standing" "double" "bus" "river" "people" "tower"

* * *

![](http://cdn.sotong.io/insta/628779a460487204c0de508ef6eb3b74.jpg)  
**Text:** "a garden with a umbrella"  
**Confidence**: 0.7961122161436683  
**Tags**: "outdoor" "building" "table" "garden" "umbrella" "stone" "roof" "sitting" "chair" "top" "wooden" "green" "area" "old" "large" "colorful" "brick" "eating" "standing" "field" "white" "bench"

* * *

![](http://cdn.sotong.io/insta/d6b2fd7b1a6438c39a5e7277c28084fe.jpg)  
**Text:** "the sky at sunset"  
**Confidence**: 0.7931825928438672  
**Tags**: "outdoor" "sunset" "water" "sun" "body" "river" "clouds" "large" "boat" "people" "city" "lake" "flying" "standing" "top" "group" "cloudy" "ocean" "airplane" "man" "field" "plane" "air" "skiing" "sky" "beach" "track" "riding"

* * *

![](http://cdn.sotong.io/insta/99c4a4a8afcde985fd87267071d44ce0.jpg)  
**Text:** "a plate of food"  
**Confidence**: 0.7920699838532201  
**Tags**: "food" "plate" "indoor" "table" "piece" "cream" "slice" "banana" "white" "top" "sitting" "fork" "cheese" "cake" "sauce" "fruit" "soup"

* * *

![](http://cdn.sotong.io/insta/efccff174880b94a930579b227b9d180.jpg)  
**Text:** "a palm tree"  
**Confidence**: 0.7909435670559972  
**Tags**: "outdoor" "tree" "plant" "palm" "grass" "flying" "park" "view" "large" "street" "people" "top" "sign" "field" "standing" "water" "green" "grassy" "tall" "air" "group" "man" "hill" "kite" "eating" "white" "blue"

* * *

![](http://cdn.sotong.io/insta/13c0cd1c7ef063c255b30668d69510f1.jpg)  
**Text:** "a donut on a white plate"  
**Confidence**: 0.7906867472844892  
**Tags**: "plate" "doughnut" "table" "food" "piece" "donut" "sitting" "snow" "dessert" "small" "white" "top" "cake" "slice" "topped" "covered" "cream" "sugar" "orange" "fruit" "pink"

* * *

![](http://cdn.sotong.io/insta/bf10bc1c350f419bd97ce5b7fb647968.jpg)  
**Text:** "a crowd of people walking down a street"  
**Confidence**: 0.7892598387454368  
**Tags**: "building" "people" "outdoor" "group" "street" "walking" "standing" "large" "crowd" "filled" "city" "many" "night" "light" "clock" "train" "riding" "red" "station" "traffic"

* * *

![](http://cdn.sotong.io/insta/1104e164b54f64ad970610e63f8a95fc.jpg)  
**Text:** "a large body of water with a city in the background"  
**Confidence**: 0.7875516332812712  
**Tags**: "water" "outdoor" "river" "city" "large" "background" "body" "ship" "boat" "bridge" "building" "day" "lake" "traveling" "train" "harbor" "floating" "cloudy" "ocean"

* * *

![](http://cdn.sotong.io/insta/8332fa134668185fbd0f6c2cca5cd63e.jpg)  
**Text:** "a glass of beer"  
**Confidence**: 0.7839422867279973  
**Tags**: "table" "indoor" "food" "sitting" "glass" "cup" "orange" "window" "beer" "wine" "hot" "white" "plate" "kitchen" "large" "restaurant" "dog"

* * *

![](http://cdn.sotong.io/insta/2e4f57a65be31e3ca56959dc356d23a1.jpg)  
**Text:** "a bench next to a tree"  
**Confidence**: 0.7810385032828375  
**Tags**: "outdoor" "grass" "bench" "tree" "plant" "park" "water" "sitting" "lake" "large" "street" "front" "view" "sign" "green" "standing" "river" "grassy" "body" "clock" "field" "parked" "man" "grazing" "people" "tower" "boat"

* * *

![](http://cdn.sotong.io/insta/90da85e08ad1bdaf3860c69a22604c02.jpg)  
**Text:** "a group of people standing in front of a restaurant"  
**Confidence**: 0.7781850987218277  
**Tags**: "person" "people" "building" "man" "front" "group" "sitting" "restaurant" "standing" "sign" "woman" "street" "light" "bar" "room" "crowd" "large" "walking" "city" "busy" "table" "television" "holding" "food" "traffic" "video" "night" "playing" "game" "motorcycle" "parked"

* * *

![](http://cdn.sotong.io/insta/6fc739a5cadade0f3a991f4971bef7be.jpg)  
**Text:** "a view of a large window"  
**Confidence**: 0.7776096172435955  
**Tags**: "window" "building" "large" "view" "sitting" "top" "table" "overlooking" "city" "plane" "airplane" "glass" "standing" "computer" "tall" "white" "bird" "man" "water" "room"

* * *

![](http://cdn.sotong.io/insta/e89760e1a937c2370074ae9645b28931.jpg)  
**Text:** "a boat on the beach"  
**Confidence**: 0.7767195710282802  
**Tags**: "outdoor" "water" "beach" "boat" "ocean" "sand" "sitting" "orange" "sunset" "red" "sandy" "shore" "top" "body" "large" "laying" "standing" "wave" "surfing" "board" "umbrella"

* * *

![](http://cdn.sotong.io/insta/2373b0514cc8f66e97b30800203d64ea.jpg)  
**Text:** "a view of a city harbor"  
**Confidence**: 0.7764506278215224  
**Tags**: "outdoor" "water" "city" "building" "river" "harbor" "large" "body" "bridge" "boat" "view" "many" "filled" "tall" "train" "clock"

* * *

![](http://cdn.sotong.io/insta/0ba2f8249c315d423b4a177e9800e9a3.jpg)  
**Text:** "a slice of cake on a plate"  
**Confidence**: 0.7752354850005562  
**Tags**: "cake" "table" "plate" "food" "piece" "chocolate" "slice" "sitting" "dessert" "cup" "top" "eaten" "cream" "desert" "white" "hydrant" "half" "knife" "cut" "close" "fruit" "fork" "covered" "cheese"

* * *

![](http://cdn.sotong.io/insta/5ba303f7e7a433bdad3574ce1e1557f9.jpg)  
**Text:** "a busy city street"  
**Confidence**: 0.772161266327658  
**Tags**: "building" "street" "outdoor" "road" "scene" "city" "sidewalk" "walking" "sign" "busy" "traffic" "car" "corner" "woman" "store" "side" "pedestrians" "man" "driving" "cross" "people" "intersection" "bus" "parked" "riding" "many" "umbrella" "decker" "holding" "tall" "double" "standing"

* * *

![](http://cdn.sotong.io/insta/bee6944b1905deeaef89869911145e47.jpg)  
**Text:** "a group of baseball players in front of a crowd"  
**Confidence**: 0.771949026833417  
**Tags**: "person" "large" "crowd" "outdoor" "grass" "player" "baseball" "group" "game" "many" "man" "front" "people" "huge" "field" "full" "standing" "bunch" "ball" "holding" "wearing" "playing" "batter" "crowded" "motorcycle" "bat"

* * *

![](http://cdn.sotong.io/insta/04ab61eba5cdbeb3f8c07ed50305d9e7.jpg)  
**Text:** "a close up of many different pictures"  
**Confidence**: 0.7719366258874463  
**Tags**: "row" "photo" "filled" "group" "sitting" "close" "lined" "black" "different" "white" "many" "wooden" "bunch" "can" "colorful" "large" "train"

* * *

![](http://cdn.sotong.io/insta/b7fb7d517c4d75c60a927555824530a9.jpg)  
**Text:** "a bird is sitting on the ground"  
**Confidence**: 0.7712931575531012  
**Tags**: "bird" "outdoor" "animal" "standing" "sitting" "brown" "small" "legs" "feet" "top" "food" "street" "side" "black" "water" "walking" "board" "chicken" "white"

* * *

![](http://cdn.sotong.io/insta/0c0be0752881b7521d7ce209025b30cd.jpg)  
**Text:** "a sandwich sitting on top of a table"  
**Confidence**: 0.7711705707915731  
**Tags**: "food" "table" "indoor" "plate" "sitting" "sandwich" "fruit" "bread" "side" "filled" "wooden" "cheese" "bowl" "salad" "cut" "fries" "white"

* * *

![](http://cdn.sotong.io/insta/3e498fc512eb60ca4dfab8461c22ea84.jpg)  
**Text:** "a garden with a bench in front of a building"  
**Confidence**: 0.7704899956028065  
**Tags**: "outdoor" "bench" "building" "stone" "grass" "park" "flower" "house" "garden" "church" "old" "front" "large" "sitting" "path" "statue" "surrounded" "clock" "walkway" "wooden" "brick" "tree" "bushes" "table" "green" "street" "tower" "standing" "woman" "tall" "fire" "white" "snow" "vase" "people" "sign" "group"

* * *

![](http://cdn.sotong.io/insta/d88b85cbcc65ed25ab8d875d41cb1d29.jpg)  
**Text:** "a beach with palm trees in the background"  
**Confidence**: 0.7697932816879252  
**Tags**: "outdoor" "beach" "water" "palm" "nature" "sandy" "ocean" "tree" "people" "board" "body" "top" "man" "umbrella" "sand" "large" "standing" "surfing" "walking" "white" "group" "flying" "clock"

* * *

![](http://cdn.sotong.io/insta/14f6a17d4d6d97ce1ae75dc0a06d7f8a.jpg)  
**Text:** "a white cat is laying on the ground"  
**Confidence**: 0.7693527700946226  
**Tags**: "cat" "white" "laying" "animal" "mammal" "indoor" "sitting" "front" "lying" "top" "dog" "black" "table" "standing" "brown" "large" "sleeping" "room"

* * *

![](http://cdn.sotong.io/insta/242d0fadec3f15aab94b0e2008ed6dc7.jpg)  
**Text:** "a plate of food with a sandwich and a cup of coffee"  
**Confidence**: 0.7688606350468923  
**Tags**: "table" "food" "cup" "plate" "indoor" "coffee" "sitting" "wooden" "sandwich" "top" "close" "cake" "fruit" "fries" "white" "hot"

* * *

![](http://cdn.sotong.io/insta/03f93f6c6e4dc8a425a67cdb44591f2d.jpg)  
**Text:** "a bowl of food on a plate"  
**Confidence**: 0.7660437939268988  
**Tags**: "plate" "food" "table" "indoor" "cup" "breakfast" "sitting" "bowl" "coffee" "meal" "small" "topped" "white" "sauce" "dish" "rice" "egg" "filled" "meat" "orange" "fruit" "cheese"

* * *

![](http://cdn.sotong.io/insta/4fcb17858d92bed7f7f97c119f1e3af4.jpg)  
**Text:** "a piece of food on a plate"  
**Confidence**: 0.763396958566349  
**Tags**: "plate" "food" "indoor" "table" "piece" "sitting" "top" "white" "slice" "sauce" "cream" "dessert" "small" "fork" "cake" "cheese" "meat" "fruit" "laying"

* * *

![](http://cdn.sotong.io/insta/27b0b33b1ea83776676e0cb0203ae62e.jpg)  
**Text:** "a large tall building with a city in the background"  
**Confidence**: 0.763183638163939  
**Tags**: "building" "outdoor" "city" "water" "large" "background" "tall" "sitting" "front" "big" "clock" "top" "standing" "tower" "castle" "river" "bird" "people" "group" "street" "riding"

* * *

![](http://cdn.sotong.io/insta/e93e582b055c0f6483190cd546d526e0.jpg)  
**Text:** "a car driving down a street next to tall buildings"  
**Confidence**: 0.7623193467968749  
**Tags**: "building" "outdoor" "road" "street" "car" "city" "driving" "traffic" "large" "sitting" "busy" "walking" "riding" "light" "tall" "top" "rug" "bus" "traveling" "parked" "red" "people" "group" "man" "standing" "drawn"

* * *

![](http://cdn.sotong.io/insta/e2bacbd578b555922641a6f285402d20.jpg)  
**Text:** "a plant in a garden"  
**Confidence**: 0.7608208813401026  
**Tags**: "plant" "outdoor" "garden" "sitting" "building" "table" "tree" "surrounded" "top" "green" "palm" "blue" "large" "water" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/afbafb00461732db79672f246eca9321.jpg)  
**Text:** "a group of people walking down a street next to a tree"  
**Confidence**: 0.760639511240882  
**Tags**: "outdoor" "road" "people" "man" "riding" "walking" "group" "street" "park" "standing" "path" "tree" "area" "trail" "woman" "holding" "city" "skiing" "hill" "hydrant" "slope"

* * *

![](http://cdn.sotong.io/insta/e3fbbcf0f5823763a938d47597947d07.jpg)  
**Text:** "a group of people on a beach with palm trees"  
**Confidence**: 0.7598121982619336  
**Tags**: "outdoor" "water" "beach" "tree" "palm" "people" "group" "ocean" "body" "large" "sun" "standing" "sandy" "walking" "several" "lake" "many" "sunset" "dog" "herd"

* * *

![](http://cdn.sotong.io/insta/3265e31a5f467202395b5980d7795702.jpg)  
**Text:** "a plate of food"  
**Confidence**: 0.7597157125456672  
**Tags**: "food" "plate" "animal" "table" "meat" "piece" "sitting" "chicken" "filled" "white" "top" "bun" "covered" "cooked" "cake" "sandwich" "pizza" "laying"

* * *

![](http://cdn.sotong.io/insta/f8597cdd858fbd06838d82cd55787777.jpg)  
**Text:** "a sunset over the water"  
**Confidence**: 0.7590240115751887  
**Tags**: "outdoor" "water" "sunset" "sun" "airplane" "clouds" "plane" "view" "flying" "large" "hill" "body" "red" "skiing" "man" "sky" "blue" "ocean" "jet" "city" "white" "air"

* * *

![](http://cdn.sotong.io/insta/cedb5e0952aa3c3d23d493026380544a.jpg)  
**Text:** "a bowl of soup and a sandwich on a plate"  
**Confidence**: 0.7589973346205802  
**Tags**: "food" "plate" "table" "bowl" "sandwich" "sauce" "cup" "white" "sitting" "soup" "dish" "side" "meal" "filled" "fries" "meat" "top" "cheese" "pasta"

* * *

![](http://cdn.sotong.io/insta/2c8864756d4cdd4be3c3ffa94248afd1.jpg)  
**Text:** "a pan filled with food"  
**Confidence**: 0.7585277246877051  
**Tags**: "food" "indoor" "table" "sitting" "pasta" "bowl" "oven" "tray" "filled" "top" "plate" "cooking" "pan" "hot" "black" "stove" "counter" "cooked" "soup" "large" "cheese" "pizza" "white" "dish"

* * *

![](http://cdn.sotong.io/insta/ac21c0cd6e37cf43d88a6d97903679d0.jpg)  
**Text:** "a view of a city skyline in the background"  
**Confidence**: 0.7585148617456101  
**Tags**: "outdoor" "building" "city" "river" "tall" "water" "large" "flying" "background" "grass" "front" "green" "view" "top" "field" "sitting" "area" "airplane" "body" "air" "lake" "plane" "park" "bridge" "bird" "clock" "standing" "group" "tower" "boat" "kite" "ocean"

* * *

![](http://cdn.sotong.io/insta/a1957cf79c86fd6a872cb051ef53b95f.jpg)  
**Text:** "a airplane that is sitting on a runway"  
**Confidence**: 0.7581685816563625  
**Tags**: "outdoor" "plane" "aircraft" "grass" "sitting" "runway" "airplane" "clouds" "sun" "top" "large" "jet" "tarmac" "view" "cloudy" "sunset" "parked" "air" "field"

* * *

![](http://cdn.sotong.io/insta/f56decc554406740fe54533c17d9012b.jpg)  
**Text:** "a group of people walking down a city street"  
**Confidence**: 0.7577688896098659  
**Tags**: "building" "scene" "outdoor" "sidewalk" "people" "street" "city" "walking" "group" "road" "standing" "man" "large" "riding" "narrow" "many" "parked" "bus" "old" "crowd" "drawn" "tall" "train"

* * *

![](http://cdn.sotong.io/insta/446da795f443187791522ff8516bf988.jpg)  
**Text:** "a close up of a tray of donuts"  
**Confidence**: 0.7566853876189235  
**Tags**: "food" "indoor" "sitting" "tray" "box" "full" "filled" "doughnut" "close" "top" "chocolate" "white" "half" "oranges" "plate" "holding" "table"

* * *

![](http://cdn.sotong.io/insta/fcdf727f0ee1818bc7fe03e653a3392f.jpg)  
**Text:** "a garden with a umbrella"  
**Confidence**: 0.7540457489734106  
**Tags**: "outdoor" "umbrella" "accessory" "chair" "table" "sitting" "set" "garden" "blue" "colorful" "holding" "large" "sun" "woman" "group" "standing" "rain" "man" "people"

* * *

![](http://cdn.sotong.io/insta/35b2e484426e9af45b0d111a4f5d8fd2.jpg)  
**Text:** "a group of people standing next to a palm tree"  
**Confidence**: 0.7490260331952402  
**Tags**: "grass" "outdoor" "palm" "tree" "plant" "park" "field" "water" "man" "bench" "people" "beach" "green" "kite" "flying" "group" "standing" "large" "top" "lined" "lake" "dog" "grassy" "laying" "walking" "red" "ocean" "playing" "tower" "riding" "air" "tall" "clock" "herd"

* * *

![](http://cdn.sotong.io/insta/9192f9d243f6209d1c42ef7f71833135.jpg)  
**Text:** "a large white bird flying over a body of water"  
**Confidence**: 0.7472679845483844  
**Tags**: "outdoor" "water" "building" "large" "flying" "plane" "bird" "body" "airplane" "small" "lake" "white" "top" "landing" "city" "jet" "boat" "air" "blue" "cloudy" "ocean" "bridge" "river" "tower"

* * *

![](http://cdn.sotong.io/insta/901d6f995d6f9f323a7aaf102d3f0789.jpg)  
**Text:** "a bench in a park"  
**Confidence**: 0.7465109136642589  
**Tags**: "outdoor" "grass" "fence" "park" "building" "bench" "sitting" "top" "sidewalk" "clock" "front" "walkway" "table" "green" "flower" "city" "view" "path" "water" "large" "garden" "street" "white" "river" "standing" "field" "people" "man"

* * *

![](http://cdn.sotong.io/insta/e408476f9a7d60155086e479ce0040d0.jpg)  
**Text:** "a large house"  
**Confidence**: 0.7456846003592407  
**Tags**: "building" "outdoor" "house" "front" "large" "sitting" "man" "area" "stone" "table" "standing" "living" "street" "clock" "woman" "brick" "old" "window" "white" "red" "tall" "riding" "room" "umbrella"

* * *

![](http://cdn.sotong.io/insta/782b5c9f4a78defc6ca117905cb05853.jpg)  
**Text:** "a close up of a slice of pizza"  
**Confidence**: 0.7456043583020449  
**Tags**: "food" "piece" "slice" "sitting" "top" "paper" "pizza" "half" "close" "small" "eaten" "laying" "wooden" "table" "cheese" "plate"

* * *

![](http://cdn.sotong.io/insta/59f7af70c33f0f95fcd4a5765ebd92c3.jpg)  
**Text:** "a dining room table"  
**Confidence**: 0.7454380956789189  
**Tags**: "chair" "table" "indoor" "sitting" "room" "dining" "building" "wooden" "small" "red" "front" "living" "furniture" "black" "umbrella" "door" "white" "standing" "bed" "vase" "water" "cat" "dog"

* * *

![](http://cdn.sotong.io/insta/818b00bfc567a919b987a53714e01e2f.jpg)  
**Text:** "a piece of bread"  
**Confidence**: 0.7442967178769264  
**Tags**: "food" "indoor" "piece" "dessert" "cake" "eaten" "cream" "sitting" "banana" "table" "doughnut" "half" "plate" "top" "donut" "slice" "covered" "paper" "desert" "bread" "filled" "close" "fruit" "sandwich" "bite" "white" "holding" "cheese" "sugar"

* * *

![](http://cdn.sotong.io/insta/706f64d8d4d0862e10cf35942f8cbb8c.jpg)  
**Text:** "a pile of fruit on display"  
**Confidence**: 0.7441548768973958  
**Tags**: "outdoor" "food" "apple" "grass" "fruit" "display" "store" "sitting" "box" "filled" "pile" "sign" "table" "displayed" "sale" "bunch" "standing" "green" "many" "produce" "large" "red" "plate" "group" "man" "white"

* * *

![](http://cdn.sotong.io/insta/97531fdba34a863f4c072d3112fd83d4.jpg)  
**Text:** "a sandwich on a plate on a table"  
**Confidence**: 0.7441124804992149  
**Tags**: "food" "plate" "table" "indoor" "sitting" "sandwich" "hot" "white" "top" "dog" "toppings"

* * *

![](http://cdn.sotong.io/insta/1ea9b724f735dac4aeca4935a54aa2ea.jpg)  
**Text:** "a group of people walking down the street in front of a store"  
**Confidence**: 0.74373143624928  
**Tags**: "building" "outdoor" "person" "road" "street" "people" "walking" "city" "standing" "group" "man" "sidewalk" "holding" "woman" "table" "store" "sign" "young" "parked" "riding" "umbrella" "room" "tall"

* * *

![](http://cdn.sotong.io/insta/8537a9f8fcab705459921af46fc54e85.jpg)  
**Text:** "a blender sitting next to a glass of wine"  
**Confidence**: 0.743404389871309  
**Tags**: "cup" "table" "glass" "sitting" "drink" "blender" "bottle" "food" "wine" "ice" "empty" "filled" "counter" "slice" "glasses" "half" "drinking" "clear" "top" "full" "cake" "water" "red" "pitcher" "fruit" "mug"

* * *

![](http://cdn.sotong.io/insta/6df442c9377088fa70e3bf867fe3b654.jpg)  
**Text:** "a large building in the city"  
**Confidence**: 0.7421488315608354  
**Tags**: "building" "outdoor" "city" "street" "road" "large" "old" "front" "tall" "big" "town" "people" "clock" "walking" "tower" "sitting" "view" "riding" "bus" "horse" "white" "busy" "driving" "drawn" "standing" "rug" "traffic" "man" "group" "parked"

* * *

![](http://cdn.sotong.io/insta/aaac6391b0504e4068a1a7f2b447b7e4.jpg)  
**Text:** "a store front"  
**Confidence**: 0.7414550859357457  
**Tags**: "building" "outdoor" "table" "sitting" "restaurant" "front" "sign" "store" "street" "bench" "large" "man" "yellow" "city" "food" "shop" "pizza" "parked" "wooden" "brick" "walking" "water" "umbrella" "train" "eating" "people" "room" "standing" "sandwich" "station"

* * *

![](http://cdn.sotong.io/insta/7022e5a6c035aca45808570654ecf782.jpg)  
**Text:** "a red and white cake on a plate"  
**Confidence**: 0.7412310618020527  
**Tags**: "table" "red" "plate" "indoor" "sitting" "cake" "top" "food" "topped" "small" "orange" "chocolate" "fire" "fruit" "birthday" "white" "hat"

* * *

![](http://cdn.sotong.io/insta/a4a5edc50f4aabc9fafe058747409732.jpg)  
**Text:** "a room with a couch and a table"  
**Confidence**: 0.7411285645154554  
**Tags**: "table" "indoor" "sitting" "room" "wooden" "small" "old" "brown" "living" "glass" "desk" "white"

* * *

![](http://cdn.sotong.io/insta/7857e496d599b70f2fe6011256e939b9.jpg)  
**Text:** "a plate of food with a banana"  
**Confidence**: 0.7411164475296945  
**Tags**: "food" "plate" "indoor" "table" "banana" "fries" "sitting" "fruit" "white" "topped" "sauce" "filled" "hot" "cheese" "cake" "bun"

* * *

![](http://cdn.sotong.io/insta/19973f3ed4447c88285ecb93d9d557e2.jpg)  
**Text:** "a plate of food and a glass of orange juice"  
**Confidence**: 0.7405121659959429  
**Tags**: "cup" "food" "table" "plate" "sitting" "red" "orange" "filled" "bowl" "sandwich" "glass" "side" "fruit" "pink" "water" "beer" "salad" "meat" "large" "hot" "oranges" "phone"

* * *

![](http://cdn.sotong.io/insta/cfec6af0eb88de0849a5a837f487e77d.jpg)  
**Text:** "a palm tree sitting next to a body of water"  
**Confidence**: 0.7397942605786587  
**Tags**: "water" "outdoor" "plant" "tree" "palm" "lake" "grass" "sitting" "body" "boat" "small" "beach" "group" "zebra" "bench" "top" "flying" "standing" "ocean" "white" "table" "green" "air" "river" "blue" "man" "sunset" "herd" "people" "tall" "field"

* * *

![](http://cdn.sotong.io/insta/fa4d28d5e71996d8bf8141cb1f087858.jpg)  
**Text:** "a bottle and a glass of beer"  
**Confidence**: 0.7397526731877861  
**Tags**: "cup" "table" "food" "bottle" "beverage" "glass" "sitting" "indoor" "drink" "ice" "beer" "banana" "filled" "counter" "top" "water" "empty" "half" "clear" "blender"

* * *

![](http://cdn.sotong.io/insta/7d7cb06d8e280ef99b472ce681b6ae9f.jpg)  
**Text:** "a large ship in the background"  
**Confidence**: 0.7387157039334855  
**Tags**: "outdoor" "ship" "boat" "truck" "large" "red" "sitting" "man" "clock" "top" "pier" "standing" "dock" "group" "snow" "white" "people" "train" "street" "light" "parked" "water" "skiing" "bus" "docked"

* * *

![](http://cdn.sotong.io/insta/54d511082fd74e52a7311877cc8569fe.jpg)  
**Text:** "a large house"  
**Confidence**: 0.7387078170368725  
**Tags**: "outdoor" "building" "house" "sitting" "clock" "front" "small" "top" "large" "table" "tree" "bushes" "garden" "green" "wooden" "street" "old" "white" "tower" "red" "riding"

* * *

![](http://cdn.sotong.io/insta/afd3c2a8a28876aef6c7c4d2743715a9.jpg)  
**Text:** "a close up of a plate of food"  
**Confidence**: 0.7381150989173921  
**Tags**: "food" "plate" "dish" "filled" "bowl" "paper" "table" "sitting" "chicken" "close" "plastic" "fruit" "hot" "white" "cheese" "meat" "bun" "dog" "holding" "sandwich"

* * *

![](http://cdn.sotong.io/insta/50b63d00922285274f0383cec83ea27d.jpg)  
**Text:** "a polar bear swimming in a pool of water"  
**Confidence**: 0.7372440415833887  
**Tags**: "bear" "water" "polar" "pool" "playing" "swimming" "dog" "large" "blue" "cat" "snow" "white"

* * *

![](http://cdn.sotong.io/insta/8b940b68e14c61812a12a4c769cf8cc3.jpg)  
**Text:** "a group of tall buildings"  
**Confidence**: 0.7365388977800968  
**Tags**: "outdoor" "building" "street" "large" "road" "old" "walking" "city" "top" "tall" "people" "many" "standing" "riding" "clock" "group" "traffic" "man" "horse" "tower" "parked"

* * *

![](http://cdn.sotong.io/insta/192993a79c8a94de8c8c71f84f215e33.jpg)  
**Text:** "a wooden cutting board topped with lots of food"  
**Confidence**: 0.735757871067298  
**Tags**: "indoor" "table" "food" "plate" "sitting" "board" "top" "cutting" "counter" "topped" "knife" "wooden" "little" "large" "eating" "hot" "laying" "kitchen" "group" "pizza"

* * *

![](http://cdn.sotong.io/insta/c3229d4e4c1b37e6a7940f6896b57ac5.jpg)  
**Text:** "a group of people standing next to a palm tree"  
**Confidence**: 0.7351495434967273  
**Tags**: "outdoor" "palm" "tree" "plant" "grass" "standing" "park" "area" "group" "top" "lined" "people" "field" "large" "beach" "covered" "dog" "man" "herd" "bench" "white" "riding" "tall" "grazing" "tower" "flying" "horse" "sign"

* * *

![](http://cdn.sotong.io/insta/5ebf57b9607e41803b5e04f26d695d0c.jpg)  
**Text:** "a breakfast sandwich and a cup of coffee"  
**Confidence**: 0.735148675443086  
**Tags**: "cup" "coffee" "table" "food" "plate" "sitting" "breakfast" "zebra" "doughnut" "small" "striped" "top" "white" "phone" "orange" "donut" "fruit" "sandwich"

* * *

![](http://cdn.sotong.io/insta/7db1bfcb41ff1a22433e839c05debfe2.jpg)  
**Text:** "a plate of food with rice and vegetables"  
**Confidence**: 0.7329265218825999  
**Tags**: "food" "plate" "table" "filled" "egg" "salad" "white" "rice" "different" "cheese" "meat" "covered" "fruit" "holding" "hot"

* * *

![](http://cdn.sotong.io/insta/5d81d151025d99e2563ae94641e30341.jpg)  
**Text:** "a view of a city skyline in the background"  
**Confidence**: 0.7323073471036295  
**Tags**: "outdoor" "building" "city" "water" "sunset" "river" "background" "cloudy" "large" "train" "sitting" "view" "track" "body" "tall" "lake" "sun" "field" "bridge" "bench" "white" "rain" "traffic" "street" "ocean" "group" "clock"

* * *

![](http://cdn.sotong.io/insta/1eddba31d14b80cce4a76d04f10605ce.jpg)  
**Text:** "a blue umbrella next to a fence"  
**Confidence**: 0.7320865974788852  
**Tags**: "umbrella" "outdoor" "fence" "accessory" "chair" "blue" "sitting" "table" "green" "rain" "colorful" "bench" "top" "water" "eating" "park" "bird" "track" "group" "people" "white" "swimming"

* * *

![](http://cdn.sotong.io/insta/02715ade2de81cdcc01809c25120aee4.jpg)  
**Text:** "a display case in a store"  
**Confidence**: 0.7305458033855737  
**Tags**: "indoor" "display" "case" "store" "window" "front" "building" "glass" "man" "shop" "woman" "standing" "table" "filled" "displayed" "large" "sign" "donut" "people" "covered" "reflection" "food" "holding" "group" "clock"

* * *

![](http://cdn.sotong.io/insta/07031263acdba7de988c0c7a195b1814.jpg)  
**Text:** "a tray of food on a table"  
**Confidence**: 0.7282330093213919  
**Tags**: "food" "table" "hot" "plate" "sitting" "cheese" "fries" "topped" "top" "bowl" "dog" "counter" "tray" "banana" "filled" "sandwich" "pizza" "hotdog" "white"

* * *

![](http://cdn.sotong.io/insta/635728f48a0ae203b36ae5148a23dea6.jpg)  
**Text:** "a store filled with lots of furniture"  
**Confidence**: 0.7252527004775416  
**Tags**: "table" "building" "indoor" "window" "food" "living" "furniture" "filled" "room" "counter" "large" "topped" "sitting" "plate" "glass" "restaurant" "display" "white" "pizza" "kitchen" "shop" "store" "standing" "group" "people"

* * *

![](http://cdn.sotong.io/insta/3f3af7d15553f5ee2a3ca6909fdf6635.jpg)  
**Text:** "a cup of coffee and a glass of beer"  
**Confidence**: 0.7237707842763572  
**Tags**: "cup" "table" "glass" "food" "drink" "sitting" "beer" "coffee" "glasses" "filled" "top" "orange" "phone" "hot" "sandwich" "tall" "woman"

* * *

![](http://cdn.sotong.io/insta/3c5e444453cebdf0032b204f8d4db17a.jpg)  
**Text:** "a blue and white boat floating on a large body of water"  
**Confidence**: 0.7236243363008671  
**Tags**: "water" "boat" "outdoor" "ocean" "lake" "reef" "blue" "floating" "body" "harbor" "large" "small" "clear" "sitting" "green" "umbrella" "people" "river" "top" "city" "pond" "beach" "flying" "group"

* * *

![](http://cdn.sotong.io/insta/da75466142235e4a3beb7ff039048a8c.jpg)  
**Text:** "a sandwich with meat and vegetables"  
**Confidence**: 0.7222181693470572  
**Tags**: "food" "sushi" "plate" "indoor" "table" "piece" "white" "paper" "slice" "topped" "top" "meat" "car" "sitting" "doughnut" "filled" "sauce" "fruit" "cut" "cutting" "holding" "cake" "sandwich" "laying"

* * *

![](http://cdn.sotong.io/insta/a14d697739b98a1ae3f234cde4c81622.jpg)  
**Text:** "a colorful parrot standing next to a fence"  
**Confidence**: 0.7213347813783815  
**Tags**: "fence" "outdoor" "bird" "water" "animal" "parrot" "sitting" "colorful" "standing" "yellow" "railing" "perched" "small" "top" "ocean" "blue" "black" "rail" "colored" "bridge" "cage" "wooden" "bench" "beach" "boat" "man" "group"

* * *

![](http://cdn.sotong.io/insta/b0341c9023bd51a0ba3f31d414f71ef2.jpg)  
**Text:** "a beach with palm trees in the background"  
**Confidence**: 0.7207336400795453  
**Tags**: "outdoor" "beach" "water" "nature" "boat" "surfing" "sitting" "people" "flying" "large" "palm" "day" "group" "man" "ocean" "sandy" "board" "body" "kite" "sand" "standing" "parked" "white"

* * *

![](http://cdn.sotong.io/insta/de10333c29b0c8c85ef116973f077cff.jpg)  
**Text:** "a red light at night"  
**Confidence**: 0.7199347015053206  
**Tags**: "building" "light" "night" "bunch" "red" "white" "sitting" "sign" "large" "hanging" "group" "station"

* * *

![](http://cdn.sotong.io/insta/fd7e89382d482becda225d4496aea02e.jpg)  
**Text:** "a plate of pasta with meat and vegetables"  
**Confidence**: 0.7197034852796313  
**Tags**: "food" "plate" "sauce" "table" "meat" "dish" "meal" "covered" "white" "topped" "sitting" "filled" "broccoli" "chicken" "pile" "top" "fries" "close" "cooked" "pasta"

* * *

![](http://cdn.sotong.io/insta/05427a886cfc5956d8f9eba9e7572077.jpg)  
**Text:** "a store front"  
**Confidence**: 0.718717922932564  
**Tags**: "building" "outdoor" "road" "street" "front" "house" "people" "town" "clock" "small" "city" "sidewalk" "large" "walking" "sitting" "sign" "parked" "store" "corner" "standing" "old" "restaurant" "shop" "brick" "man" "woman" "stop" "group" "white" "red" "riding" "tall" "window"

* * *

![](http://cdn.sotong.io/insta/111f653bf01b7b8c518ef96132970cde.jpg)  
**Text:** "a night scene with a building in the background"  
**Confidence**: 0.7178907222207381  
**Tags**: "building" "outdoor" "night" "light" "lit" "city" "large" "sitting" "filled" "red" "orange" "harbor" "white" "table" "standing" "street" "water" "parked"

* * *

![](http://cdn.sotong.io/insta/1800456b491ca48d58ec669ae65e1900.jpg)  
**Text:** "a close up of a pizza with cheese and vegetables"  
**Confidence**: 0.717839859500786  
**Tags**: "pizza" "food" "cheese" "top" "toppings" "close" "sitting" "covered" "large" "plate" "meat" "water" "table" "broccoli" "white" "cooked" "pan"

* * *

![](http://cdn.sotong.io/insta/cb2a24b406fd9622dd25b9b8c41a5c90.jpg)  
**Text:** "a piece of meat on a white plate"  
**Confidence**: 0.7171500482692051  
**Tags**: "plate" "food" "table" "indoor" "meat" "white" "sitting" "cake" "fork" "piece" "top" "eaten" "topped" "rice" "dinner" "broccoli" "chocolate" "holding" "laying"

* * *

![](http://cdn.sotong.io/insta/91f77846588cb4ff4c4e9ffa56439e06.jpg)  
**Text:** "a garden with a bench in front of a tree"  
**Confidence**: 0.71578361053758  
**Tags**: "outdoor" "building" "tree" "garden" "sitting" "bench" "wooden" "palm" "red" "park" "bushes" "flower" "front" "surrounded" "table" "large" "top" "green" "street" "forest" "white" "sign" "colorful" "phone" "parked" "tall"

* * *

![](http://cdn.sotong.io/insta/f9f2a32ea05addfa5751e30c8d1ffa4b.jpg)  
**Text:** "a street in front of a church"  
**Confidence**: 0.715086283604722  
**Tags**: "road" "outdoor" "building" "street" "church" "old" "large" "city" "front" "intersection" "walking" "driving" "side" "riding" "sitting" "stone" "clock" "parked" "stop" "white" "lot" "tall" "traffic" "carriage" "parking" "fire" "sign" "drawn" "tower" "horse" "people"

* * *

![](http://cdn.sotong.io/insta/bc4a9da27c57058fedd37788632a2274.jpg)  
**Text:** "a group of people standing in front of a building"  
**Confidence**: 0.7143145589289609  
**Tags**: "building" "outdoor" "sidewalk" "bench" "front" "people" "man" "park" "group" "stone" "standing" "walking" "woman" "large" "sitting" "clock" "table" "young" "statue" "garden" "snow" "riding" "city" "street" "playing" "parked" "tower" "white"

* * *

![](http://cdn.sotong.io/insta/5625022b4b6a43f6fa5648fcf66ab6b9.jpg)  
**Text:** "a plane flying through a cloudy blue sky"  
**Confidence**: 0.7121344335733453  
**Tags**: "outdoor" "flying" "plane" "cloudy" "blue" "airplane" "air" "clouds" "large" "jet" "high" "bird" "city" "white"

* * *

![](http://cdn.sotong.io/insta/e0fdbc5377a66fbe72bc74c6d8c48cc0.jpg)  
**Text:** "a piece of chocolate cake"  
**Confidence**: 0.7116157481713158  
**Tags**: "cake" "piece" "table" "food" "chocolate" "sitting" "dessert" "slice" "top" "paper" "cup" "coffee" "cream" "plate" "close" "large"

* * *

![](http://cdn.sotong.io/insta/fa2f9dae027613946c153fe494607c14.jpg)  
**Text:** "a view of a living room with a large window"  
**Confidence**: 0.7109996945256474  
**Tags**: "window" "indoor" "room" "building" "living" "table" "view" "large" "water" "sitting" "overlooking" "open" "furniture" "area" "television" "river" "bedroom" "sun" "glass" "black" "ocean" "door" "city"

* * *

![](http://cdn.sotong.io/insta/931505eb481bf7b23b65d9df91b5b33a.jpg)  
**Text:** "a group of people standing on a sidewalk"  
**Confidence**: 0.7101432158275924  
**Tags**: "person" "building" "outdoor" "man" "group" "people" "standing" "street" "suit" "sidewalk" "city" "walking" "holding" "young" "talking" "dressed" "wedding"

* * *

![](http://cdn.sotong.io/insta/91bc9d53ec009cdc1606bdc0bf908831.jpg)  
**Text:** "a view of a city bridge"  
**Confidence**: 0.709889834662207  
**Tags**: "outdoor" "city" "water" "building" "river" "bridge" "large" "view" "bench" "tall" "park" "riding" "boat" "clock" "body" "sunset" "ocean" "flying" "man" "air" "road"

* * *

![](http://cdn.sotong.io/insta/791766c8e0af4863a9f2b1f8888c80dc.jpg)  
**Text:** "a piece of meat and vegetables"  
**Confidence**: 0.7097218083023329  
**Tags**: "food" "sitting" "table" "top" "piece" "plate" "fruit" "cake" "topped" "chicken" "chocolate" "banana" "meat" "sandwich" "board" "cutting" "pan"

* * *

![](http://cdn.sotong.io/insta/aa32e0944a175d7eb5d56a322ce29522.jpg)  
**Text:** "a boat sitting next to a glass of water"  
**Confidence**: 0.7095220399695608  
**Tags**: "water" "outdoor" "table" "boat" "sitting" "chair" "large" "window" "building" "ocean" "overlooking" "pier" "green" "top" "dock" "umbrella" "glass" "body" "docked" "city" "bird" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/ca1d2a2d088e2dc8a2a58c954025ba54.jpg)  
**Text:** "a view of a body of water filled with boats"  
**Confidence**: 0.708042406909218  
**Tags**: "water" "outdoor" "river" "boat" "body" "harbor" "city" "view" "large" "ocean" "bridge" "filled" "many" "sitting" "lake" "group" "docked" "people" "parked"

* * *

![](http://cdn.sotong.io/insta/2424a1b19d303c7d1ec63595648548ad.jpg)  
**Text:** "a boat is docked next to a bridge"  
**Confidence**: 0.7076775729349599  
**Tags**: "water" "outdoor" "boat" "bridge" "large" "river" "ship" "sitting" "harbor" "docked" "long" "top" "city" "riding" "traveling" "white" "blue"

* * *

![](http://cdn.sotong.io/insta/cda2ed461666e008b772d7e719c129a2.jpg)  
**Text:** "a slice of pizza"  
**Confidence**: 0.7070873323108281  
**Tags**: "food" "slice" "piece" "table" "sitting" "top" "plate" "car" "red" "cake" "covered" "topped" "fruit" "banana" "cheese" "pizza" "white" "laying" "snow" "pan"

* * *

![](http://cdn.sotong.io/insta/1482937d194db64a4866c697ac8bbdf7.jpg)  
**Text:** "a boat is docked next to a dock"  
**Confidence**: 0.7043262861478674  
**Tags**: "outdoor" "boat" "water" "dock" "harbor" "small" "sitting" "docked" "pier" "group" "parked" "table" "yellow" "large" "old" "river" "bridge" "standing" "people" "man"

* * *

![](http://cdn.sotong.io/insta/5308bf0c611d38952d66ad76b8f3ce01.jpg)  
**Text:** "a group of people walking down a street"  
**Confidence**: 0.703025982935664  
**Tags**: "building" "people" "person" "group" "walking" "city" "street" "standing" "large" "sidewalk" "train" "many" "woman" "man" "riding" "holding" "crowd" "road" "snow"

* * *

![](http://cdn.sotong.io/insta/81756b1c5f24e65f943bce8f1f8548a3.jpg)  
**Text:** "a large flat screen tv"  
**Confidence**: 0.7014963501853549  
**Tags**: "monitor" "television" "screen" "indoor" "show" "man" "front" "sign" "watching" "computer" "photo" "sitting" "large" "standing" "display" "table" "giving" "flat" "top" "blue" "crowd" "cat" "laptop" "video" "people" "holding" "white" "keyboard" "woman" "remote" "game" "soccer" "playing" "board" "player" "room"

* * *

![](http://cdn.sotong.io/insta/fb20d195f440d9d6f339ca7921c51d83.jpg)  
**Text:** "a flock of birds flying over a body of water"  
**Confidence**: 0.7014321205198514  
**Tags**: "outdoor" "nature" "water" "flying" "large" "ocean" "grass" "people" "many" "full" "city" "field" "body" "group" "beach" "view" "lot" "filled" "top" "hill" "cloudy" "blue" "standing" "kite" "air" "grassy" "bird" "crowd" "flock" "crowded"

* * *

![](http://cdn.sotong.io/insta/253bc21a8bdbc7a7cfc384deb69241e4.jpg)  
**Text:** "a harbor filled with clouds"  
**Confidence**: 0.697926259415088  
**Tags**: "outdoor" "water" "boat" "scene" "cloudy" "clouds" "harbor" "river" "docked" "ship" "large" "background" "dock" "body" "pier" "day" "sun" "city" "bridge" "floating" "several" "sunset" "blue" "parked" "group" "ocean" "clock" "tower"

* * *

![](http://cdn.sotong.io/insta/e0dbaf79fccdec0f15c2ffb0ad022f49.jpg)  
**Text:** "a view of a mountain"  
**Confidence**: 0.6977583708417664  
**Tags**: "outdoor" "mountain" "grass" "green" "field" "view" "bench" "water" "hill" "sitting" "top" "grazing" "grassy" "bushes" "large" "hillside" "wooden" "standing" "river" "sign" "tree" "rocky" "brick"

* * *

![](http://cdn.sotong.io/insta/0b8699289c5928841f07eef39fd3ddf8.jpg)  
**Text:** "a piece of food"  
**Confidence**: 0.69728940372817  
**Tags**: "food" "table" "sushi" "indoor" "plate" "piece" "sitting" "coffee" "slice" "top" "paper" "dessert" "topped" "cream" "small" "sandwich" "hot" "fork" "cake" "donut" "cheese" "fruit" "covered" "white" "hotdog" "meat" "bun" "red" "laying"

* * *

![](http://cdn.sotong.io/insta/e9ac8a126345f1a67f7a04a2c4724862.jpg)  
**Text:** "a close up of a pizza on a cutting board"  
**Confidence**: 0.6971040704431734  
**Tags**: "food" "pizza" "piece" "wooden" "slice" "board" "cutting" "table" "top" "sitting" "cheese" "plate" "close" "toppings" "white" "cut" "cooked" "broccoli" "laying"

* * *

![](http://cdn.sotong.io/insta/17ff0ced40d75e4fbf44774ee597845f.jpg)  
**Text:** "a white plate topped with meat and fruit"  
**Confidence**: 0.6955147769123243  
**Tags**: "plate" "food" "table" "white" "filled" "sitting" "topped" "fruit" "meat" "top" "full" "covered" "banana" "oranges" "bowl"

* * *

![](http://cdn.sotong.io/insta/a11d406f74078dd6b2395a1908434689.jpg)  
**Text:** "a group of people standing in front of a store"  
**Confidence**: 0.6949485308827777  
**Tags**: "person" "people" "table" "man" "group" "food" "restaurant" "sitting" "standing" "front" "bar" "eating" "store" "woman" "sign" "display" "crowded" "crowd" "shop" "young" "holding" "plate" "white" "phone" "pizza"

* * *

![](http://cdn.sotong.io/insta/a75e3b408b3f3a19b945c26597523f10.jpg)  
**Text:** "a painting of a brick building"  
**Confidence**: 0.6897705869974361  
**Tags**: "building" "brick" "sitting" "painting" "bird" "holding" "standing" "large" "red" "man" "graffiti"

* * *

![](http://cdn.sotong.io/insta/c3167dc55e757cb799f3f06f14b7d610.jpg)  
**Text:** "a bird is standing on a cloudy day"  
**Confidence**: 0.6869343527909485  
**Tags**: "outdoor" "standing" "cloudy" "clouds" "looking" "top" "field" "day" "grass" "background" "bird" "high" "sitting" "flying" "grassy" "hill" "large" "tree" "tall" "people" "air" "kite" "blue"

* * *

![](http://cdn.sotong.io/insta/170c2dc60cf74bcd5cdf142d754701b8.jpg)  
**Text:** "a view of a city with tall buildings"  
**Confidence**: 0.6866056749283214  
**Tags**: "building" "outdoor" "city" "train" "background" "water" "small" "street" "large" "area" "sitting" "top" "view" "tall" "red" "green" "track" "table" "bench" "river" "white" "field" "riding" "bus"

* * *

![](http://cdn.sotong.io/insta/2ff2243f34a608791ad8cf888fecaffd.jpg)  
**Text:** "a street filled with traffic at night on a rainy day"  
**Confidence**: 0.6863230106856472  
**Tags**: "building" "nature" "outdoor" "street" "rain" "car" "traffic" "rainy" "filled" "water" "city" "night" "wet" "busy" "many" "walking" "bunch" "group" "light" "driving" "large" "holding" "standing" "people"

* * *

![](http://cdn.sotong.io/insta/51c9d91b3036857d692c75a3bc89943c.jpg)  
**Text:** "a garden filled with lots of green grass"  
**Confidence**: 0.6854213771839884  
**Tags**: "outdoor" "grass" "green" "field" "large" "grassy" "bushes" "many" "sign" "tree" "garden" "forest" "group" "traveling" "street" "track" "city" "standing" "train" "people" "tall" "red" "hill" "parked" "riding"

* * *

![](http://cdn.sotong.io/insta/cfc4a03ceaca905c49913c125b314798.jpg)  
**Text:** "a bowl of food on a table"  
**Confidence**: 0.6846847274383604  
**Tags**: "food" "sashimi" "table" "indoor" "plate" "sitting" "top" "meat" "coffee" "bowl" "black" "small" "glass" "wooden" "cake" "hot" "red" "baked" "close" "green" "brown" "pan" "rice" "broccoli"

* * *

![](http://cdn.sotong.io/insta/77f6e20d16b63db72b9beb1547f60bf8.jpg)  
**Text:** "a fire place sitting in front of a brick building"  
**Confidence**: 0.6841384308744506  
**Tags**: "building" "indoor" "living" "fireplace" "room" "brick" "table" "stone" "fire" "sitting" "chair" "place" "area" "front" "white" "furniture" "old" "street" "light" "large" "pizza" "television" "man" "standing" "oven" "city" "toilet" "sign"

* * *

![](http://cdn.sotong.io/insta/1fc971234e6c10c4c030a9027a925fbe.jpg)  
**Text:** "a large body of water with a city in the background"  
**Confidence**: 0.6835550708140441  
**Tags**: "outdoor" "building" "city" "water" "river" "large" "background" "harbor" "bridge" "top" "cloudy" "tall" "view" "group" "green" "park" "bench" "body" "riding" "people" "flying" "ocean"

* * *

![](http://cdn.sotong.io/insta/6041e7f7157994a131827f3e65dea5b4.jpg)  
**Text:** "a woman posing for a picture"  
**Confidence**: 0.6821404933703812  
**Tags**: "person" "woman" "outdoor" "standing" "holding" "photo" "people" "posing" "wearing" "street" "girl" "dress" "black" "young" "man" "city" "group" "walking" "phone" "white"

* * *

![](http://cdn.sotong.io/insta/a41685797a4dbd9ff7210f96aa212ad3.jpg)  
**Text:** "a group of people walking on a city street filled with traffic at night"  
**Confidence**: 0.6796883567555235  
**Tags**: "building" "outdoor" "street" "night" "city" "walking" "filled" "light" "many" "people" "table" "standing" "man" "bunch" "sign" "covered" "traffic" "woman" "store" "holding" "group" "parked" "room"

* * *

![](http://cdn.sotong.io/insta/ffba44da7c7f44809b2126bd9d8b982a.jpg)  
**Text:** "a plate of food with broccoli"  
**Confidence**: 0.6793538983774001  
**Tags**: "plate" "food" "indoor" "table" "meat" "white" "piece" "broccoli" "sitting" "topped" "dinner" "water" "knife" "laying"

* * *

![](http://cdn.sotong.io/insta/472dd30faad193168c480bc20bd4c1ec.jpg)  
**Text:** "a bowl of food on a pan"  
**Confidence**: 0.6785304116314035  
**Tags**: "food" "table" "black" "bowl" "sitting" "pan" "top" "pot" "plate" "filled" "stove" "wooden" "meat" "large" "green" "cooking" "soup" "broccoli" "dish"

* * *

![](http://cdn.sotong.io/insta/a9d5b377500ad830421bec7ae8ab3f63.jpg)  
**Text:** "a car driving down a street next to tall buildings"  
**Confidence**: 0.6783103729910752  
**Tags**: "outdoor" "building" "road" "street" "car" "city" "traffic" "light" "old" "large" "driving" "church" "busy" "tall" "green" "walking" "bus" "parked" "people" "intersection" "riding" "traveling" "standing" "drawn" "red" "group" "double" "horse" "tower" "sign" "clock" "decker" "white"

* * *

![](http://cdn.sotong.io/insta/87012d0a5c915e209f2cd5f3bac8b431.jpg)  
**Text:** "a large tall building with a kite"  
**Confidence**: 0.67822953486614  
**Tags**: "outdoor" "building" "large" "flying" "tower" "street" "kite" "clock" "town" "church" "city" "people" "standing" "old" "tall" "field" "group" "walking" "parked" "road" "blue"

* * *

![](http://cdn.sotong.io/insta/ae580d4f4dd9a860824949f56d3c9e80.jpg)  
**Text:** "a plate of food and a bowl of fruit"  
**Confidence**: 0.6780654994725676  
**Tags**: "food" "plate" "table" "sitting" "bowl" "fruit" "small" "top" "filled" "banana" "brown" "wooden" "white" "meat" "holding"

* * *

![](http://cdn.sotong.io/insta/77b078cea4661d42caf99595754851e3.jpg)  
**Text:** "a pile of food on display"  
**Confidence**: 0.6778004758202779  
**Tags**: "indoor" "food" "table" "sitting" "large" "filled" "wooden" "different" "fries" "display" "pile" "board" "holding" "cut" "plate" "cutting" "pizza" "sign"

* * *

![](http://cdn.sotong.io/insta/55a8a80767d8ba4de9ce8be33c804c25.jpg)  
**Text:** "sunset at the beach"  
**Confidence**: 0.6767376151287562  
**Tags**: "outdoor" "beach" "water" "sunset" "ocean" "surfing" "sun" "sitting" "sand" "standing" "sandy" "board" "top" "man" "boat" "track" "body" "large" "wave" "umbrella" "red" "people" "flying" "group" "air" "parked"

* * *

![](http://cdn.sotong.io/insta/cf355f5b2fc5104629726c8fb9b3dbd8.jpg)  
**Text:** "a cake made to look like a birthday cake"  
**Confidence**: 0.6757249152818924  
**Tags**: "cake" "table" "indoor" "birthday" "plate" "top" "food" "decorated" "sitting" "made" "chocolate" "topped" "large" "boy" "covered" "white" "cream" "toppings" "train"

* * *

![](http://cdn.sotong.io/insta/925b8e192275eafaf007a5b2d3359e9a.jpg)  
**Text:** "a tall brick building sitting next to a fire hydrant"  
**Confidence**: 0.6740305597967673  
**Tags**: "outdoor" "building" "grass" "hydrant" "brick" "old" "fire" "sitting" "front" "stone" "street" "tower" "sidewalk" "side" "sign" "large" "tall" "standing" "red" "water" "green" "field" "parked" "city" "clock" "white" "grassy" "sheep"

* * *

![](http://cdn.sotong.io/insta/c2f2a68c361c4db54a0cde0331bc1969.jpg)  
**Text:** "a group of people standing in front of a crowd"  
**Confidence**: 0.673292560930595  
**Tags**: "person" "people" "outdoor" "crowd" "group" "standing" "sitting" "front" "light" "crowded" "man" "food" "large" "street" "busy" "table" "many" "walking" "sign" "city" "umbrella" "traffic"

* * *

![](http://cdn.sotong.io/insta/afbe923620bec0872b046d41161a407b.jpg)  
**Text:** "a group of people standing outside of a restaurant"  
**Confidence**: 0.6714358999569623  
**Tags**: "person" "building" "table" "people" "man" "group" "food" "standing" "bar" "restaurant" "wine" "sitting" "filled" "sign" "woman" "walking" "large" "street"

* * *

![](http://cdn.sotong.io/insta/b667a3610cb839dd4ff27c6d12c35500.jpg)  
**Text:** "a view of a beach"  
**Confidence**: 0.6692577646502536  
**Tags**: "outdoor" "grass" "water" "view" "ocean" "large" "hill" "overlooking" "beach" "blue" "green" "sitting" "lot" "city" "field" "mountain" "many" "body" "colorful" "busy" "people" "umbrella" "white" "sign" "sheep" "parked"

* * *

![](http://cdn.sotong.io/insta/82312e44fe4c3dd5f7cdab30c276475c.jpg)  
**Text:** "a display in a store"  
**Confidence**: 0.6687877156546106  
**Tags**: "indoor" "table" "sitting" "computer" "top" "desk" "monitor" "large" "clock" "white" "store" "display" "group"

* * *

![](http://cdn.sotong.io/insta/b381ce5bf6cf2caef555029becdb651b.jpg)  
**Text:** "a group of people standing outside of a building"  
**Confidence**: 0.665635838437293  
**Tags**: "person" "building" "people" "indoor" "luggage" "suitcase" "walking" "group" "standing" "man" "woman" "bag" "waiting" "large" "station" "table" "room" "train" "holding" "red" "crowd" "fire"

* * *

![](http://cdn.sotong.io/insta/8f5d52b226dbfa2745376a1d169944ab.jpg)  
**Text:** "a view of a city with tall buildings"  
**Confidence**: 0.6636262768812939  
**Tags**: "outdoor" "building" "city" "large" "view" "traffic" "street" "background" "tall" "light" "highway" "boat" "green" "busy" "water" "tower" "bridge" "river" "sign" "white"

* * *

![](http://cdn.sotong.io/insta/ff4854e0d46c40d1871961402110bbf4.jpg)  
**Text:** "a close up of a tray of donuts"  
**Confidence**: 0.6623682124832059  
**Tags**: "indoor" "food" "tray" "sitting" "half" "filled" "table" "full" "topped" "plate" "white" "close" "banana" "several" "pepperoni" "large"

* * *

![](http://cdn.sotong.io/insta/0ffc650dc133f66e8823075462ebf1c3.jpg)  
**Text:** "a view of a beach"  
**Confidence**: 0.6589256001971134  
**Tags**: "outdoor" "water" "nature" "beach" "ocean" "top" "large" "flying" "man" "air" "standing"

* * *

![](http://cdn.sotong.io/insta/cbca1400becf7b1058ec7939dc169cc8.jpg)  
**Text:** "a group of people walking down a dirt road"  
**Confidence**: 0.6575309038903007  
**Tags**: "outdoor" "grass" "dirt" "truck" "parked" "group" "line" "row" "lined" "forest" "path" "area" "side" "people" "tree" "standing" "many" "walking" "field"

* * *

![](http://cdn.sotong.io/insta/083fbd93d186924893fe563064c065e4.jpg)  
**Text:** "a statue of a tall building"  
**Confidence**: 0.6571975592689444  
**Tags**: "outdoor" "building" "large" "front" "clock" "church" "top" "stone" "sitting" "standing" "tall" "tower" "old" "big" "statue" "white" "city" "street" "woman" "parked" "man" "people"

* * *

![](http://cdn.sotong.io/insta/2e7f4bdc08b7493e4a277e924bb3683c.jpg)  
**Text:** "a small boat in a large city"  
**Confidence**: 0.6562839101489157  
**Tags**: "boat" "outdoor" "water" "building" "dock" "filled" "ship" "large" "sitting" "pier" "docked" "small" "city" "harbor" "top" "river" "body" "many" "people" "group" "old" "table" "man" "white" "bridge" "flock" "standing"

* * *

![](http://cdn.sotong.io/insta/5fe5f0f912f8f15674e8821f884b0be2.jpg)  
**Text:** "a close up of a sandwich and french fries"  
**Confidence**: 0.6550730947617105  
**Tags**: "food" "fries" "indoor" "sandwich" "sitting" "plate" "dog" "table" "hot" "bun" "paper" "top" "close" "pile" "large" "hotdog" "cheese" "white"

* * *

![](http://cdn.sotong.io/insta/1eee459b167657f9e421125d31ad1c9e.jpg)  
**Text:** "a herd of giraffe standing next to a tree"  
**Confidence**: 0.6547036256970944  
**Tags**: "giraffe" "outdoor" "standing" "animal" "mammal" "grass" "group" "eating" "grazing" "herd" "field" "food" "zoo" "area" "grassy" "walking" "enclosure" "green" "tall" "zebra"

* * *

![](http://cdn.sotong.io/insta/96297ed1c4c6060397b5e09602e99234.jpg)  
**Text:** "a coffee cup sitting on a table"  
**Confidence**: 0.6543127308481638  
**Tags**: "cup" "table" "sitting" "coffee" "drink" "food" "glass" "beer" "orange" "computer" "top" "laptop" "red" "dog" "laying"

* * *

![](http://cdn.sotong.io/insta/7911059c9b4b5f52591b0ebccdd15f9d.jpg)  
**Text:** "a boat is docked next to a large body of water"  
**Confidence**: 0.6541927489199566  
**Tags**: "water" "outdoor" "boat" "pier" "large" "body" "ship" "sitting" "city" "lake" "building" "bridge" "river" "view" "dock" "docked" "harbor" "bird" "filled" "overlooking" "green" "many" "group" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/53f39908d7e34c32eacf2419b11af4b6.jpg)  
**Text:** "a fire place sitting in front of a brick building"  
**Confidence**: 0.6532871974120962  
**Tags**: "building" "fire" "brick" "fireplace" "living" "photo" "place" "room" "red" "sitting" "woman" "door" "front" "man" "table" "orange" "old" "standing" "playing" "colorful" "pizza" "holding" "street" "covered" "painted" "dog" "large" "people" "white" "yellow" "graffiti" "wall" "game" "hydrant"

* * *

![](http://cdn.sotong.io/insta/46f69000932723879f6bf234ebe8178a.jpg)  
**Text:** "a green umbrella"  
**Confidence**: 0.6532855720577223  
**Tags**: "grass" "green" "outdoor" "elephant" "fabric" "sitting" "set" "table" "top" "front" "large" "painted" "face" "umbrella" "cat" "people" "standing" "old" "stop" "covered" "man" "field" "horse"

* * *

![](http://cdn.sotong.io/insta/931a2fedb59327337277154bbe89e64d.jpg)  
**Text:** "a coffee cup sitting on a table"  
**Confidence**: 0.647335062025319  
**Tags**: "cup" "table" "sitting" "coffee" "drink" "food" "glass" "orange" "beer" "top" "computer" "laptop" "red" "laying"

* * *

![](http://cdn.sotong.io/insta/944bd4d35a92a09822cb94faa0afcef0.jpg)  
**Text:** "a coffee cup sitting on a table"  
**Confidence**: 0.6471886752676399  
**Tags**: "cup" "table" "coffee" "sitting" "indoor" "food" "drink" "beverage" "doughnut" "donut" "glass" "front" "top" "spoon" "computer" "plate" "milk" "laptop" "hot" "cake" "mug" "white" "pitcher"

* * *

![](http://cdn.sotong.io/insta/7df88284b0319f6597f1a28b0a454d84.jpg)  
**Text:** "a dining room table in a restaurant"  
**Confidence**: 0.6441019676355946  
**Tags**: "table" "indoor" "chair" "building" "ceiling" "dining" "room" "restaurant" "window" "sitting" "filled" "food" "large" "furniture" "area" "white" "bar" "several" "many" "covered" "library" "glass" "standing" "plate" "people" "group" "display" "kitchen"

* * *

![](http://cdn.sotong.io/insta/7af38e03d5cb80340d33f39f403b9050.jpg)  
**Text:** "a cup of coffee and a glass of wine"  
**Confidence**: 0.6406799699025999  
**Tags**: "cup" "table" "food" "drink" "beverage" "glass" "coffee" "sitting" "filled" "drinking" "plate" "glasses" "full" "water" "pitcher" "holding" "sandwich"

* * *

![](http://cdn.sotong.io/insta/923a93dab6b76fb85941f4d8789a6d1b.jpg)  
**Text:** "a close up of a pizza on a paper plate"  
**Confidence**: 0.6401690451803878  
**Tags**: "food" "table" "plate" "indoor" "sitting" "top" "white" "paper" "piece" "topped" "sandwich" "close" "cake" "cheese" "cut" "pizza"

* * *

![](http://cdn.sotong.io/insta/c868cee3ccf460d8f52f34bee85270de.jpg)  
**Text:** "a tree next to a palm tree"  
**Confidence**: 0.636952692703352  
**Tags**: "outdoor" "plant" "tree" "palm" "standing" "shade" "zebra" "water" "snow" "area" "sandy" "sitting" "bench" "field" "beach" "walking" "park" "herd" "man" "top" "covered" "large" "group" "people" "grazing" "dirt" "tall" "street" "giraffe"

* * *

![](http://cdn.sotong.io/insta/84a7f99b4f63ae86c45e092e31d88660.jpg)  
**Text:** "a large tree"  
**Confidence**: 0.6363581469431249  
**Tags**: "grass" "outdoor" "field" "sheep" "standing" "herd" "grazing" "large" "group" "mountain" "front" "lake" "overlooking" "man" "pasture" "cow" "flower" "green" "people" "flock" "grassy" "hill" "horse" "water" "bench" "tree" "rain" "city" "cattle" "street" "river" "tall"

* * *

![](http://cdn.sotong.io/insta/76d285c21d1225c8ed427fe3b857c2e0.jpg)  
**Text:** "a plate of food with a sandwich and french fries"  
**Confidence**: 0.6349465318489228  
**Tags**: "food" "plate" "table" "fries" "sitting" "side" "sandwich" "filled" "meat" "holding" "cut" "white"

* * *

![](http://cdn.sotong.io/insta/d6a5ca2df963bed45e436f4cccdc2b0b.jpg)  
**Text:** "a castle with a body of water"  
**Confidence**: 0.6345197953837386  
**Tags**: "outdoor" "water" "nature" "grass" "river" "lake" "large" "sitting" "pond" "body" "small" "front" "red" "green" "city" "train" "parked" "bridge" "white" "castle" "flying"

* * *

![](http://cdn.sotong.io/insta/ebcdd85d7017048099b94dd8a2b7915b.jpg)  
**Text:** "a piece of fruit"  
**Confidence**: 0.6332498388020557  
**Tags**: "food" "fruit" "plate" "table" "topped" "slice" "banana" "sitting" "piece" "filled" "orange" "cheese" "sauce" "top" "white" "oranges" "covered" "holding" "hot" "purple" "laying"

* * *

![](http://cdn.sotong.io/insta/4687c4c96481a5199d512042c4656f4b.jpg)  
**Text:** "a group of palm trees"  
**Confidence**: 0.630510398979341  
**Tags**: "outdoor" "grass" "tree" "palm" "green" "sitting" "field" "large" "umbrella" "covered" "group" "table" "yellow" "fruit" "garden" "standing" "tall"

* * *

![](http://cdn.sotong.io/insta/54217097a39e46576ce45df6213e4e96.jpg)  
**Text:** "a statue of a garden"  
**Confidence**: 0.6274158645898834  
**Tags**: "grass" "outdoor" "building" "lawn" "sitting" "table" "park" "sidewalk" "front" "street" "white" "green" "garden" "top" "tree" "small" "yard" "bench" "large" "flower" "standing" "statue" "clock" "sign" "walking" "old" "fire" "man" "umbrella" "field" "hydrant"

* * *

![](http://cdn.sotong.io/insta/f3056848337e586b885a7207b7c7628c.jpg)  
**Text:** "a bowl filled with meat and vegetables"  
**Confidence**: 0.6241800591660477  
**Tags**: "food" "table" "plate" "indoor" "bowl" "sitting" "meat" "top" "filled" "meal" "rice" "full" "black" "different" "broccoli" "green" "fruit" "white" "stove"

* * *

![](http://cdn.sotong.io/insta/77bede97b2d617400b8e9d2e5649d81d.jpg)  
**Text:** "a group of people sitting at a table in a restaurant"  
**Confidence**: 0.6239814827082912  
**Tags**: "table" "building" "people" "sitting" "food" "restaurant" "filled" "group" "light" "room" "dining" "lit" "night" "many" "standing" "umbrella" "man" "display" "street" "plate" "sign" "city"

* * *

![](http://cdn.sotong.io/insta/8d52ef7d5f4f7af14106749fe2a5c118.jpg)  
**Text:** "a display of a cake"  
**Confidence**: 0.622496071933762  
**Tags**: "indoor" "food" "cake" "table" "sitting" "fruit" "chocolate" "top" "different" "display" "bunch" "plate" "sign"

* * *

![](http://cdn.sotong.io/insta/e77e019055428ca50b47069d50799ed7.jpg)  
**Text:** "a garden with a blue umbrella"  
**Confidence**: 0.622477133934236  
**Tags**: "outdoor" "fence" "blue" "table" "bench" "sitting" "park" "umbrella" "building" "water" "resort" "parked" "front" "pool" "wooden" "flower" "garden" "green" "large" "dock" "street" "standing" "white" "boat"

* * *

![](http://cdn.sotong.io/insta/ba6e92ed38fffa51a8ff5f64050c6c29.jpg)  
**Text:** "a city at night"  
**Confidence**: 0.6213788534859523  
**Tags**: "city" "building" "large" "filled" "night" "circuit" "light" "many" "water" "traffic"

* * *

![](http://cdn.sotong.io/insta/551af00f8d5c721b0f8b3d45a25c7639.jpg)  
**Text:** "a table with a cake"  
**Confidence**: 0.6204018235286511  
**Tags**: "table" "cake" "sitting" "window" "building" "large" "top" "water" "desk" "computer" "glass" "light" "laptop" "cutting" "man" "dog" "white"

* * *

![](http://cdn.sotong.io/insta/8b4d383b81234e35ec84a89302c4ddce.jpg)  
**Text:** "a tree filled forest"  
**Confidence**: 0.619614809232568  
**Tags**: "outdoor" "rock" "forest" "tree" "trail" "path" "area" "standing" "wood" "small" "sitting" "large" "dirt" "walking" "black" "park" "giraffe" "bench" "rocky" "eating" "enclosure" "zebra" "water" "zoo"

* * *

![](http://cdn.sotong.io/insta/08dcad9ea5be3cc1c4c3c97a6852b456.jpg)  
**Text:** "a crowd of people standing outside of a building"  
**Confidence**: 0.6173882506872587  
**Tags**: "building" "road" "outdoor" "people" "walking" "group" "large" "street" "city" "standing" "crowd" "many" "lot" "riding" "traffic" "man" "clock" "bus" "parked"

* * *

![](http://cdn.sotong.io/insta/2ffe8eb5e5461512504dcbdf0698c77b.jpg)  
**Text:** "a room filled with furniture and a table in a restaurant"  
**Confidence**: 0.6172762988122945  
**Tags**: "table" "chair" "room" "filled" "restaurant" "large" "sitting" "living" "furniture" "people" "train"

* * *

![](http://cdn.sotong.io/insta/3790a497024e1916aa0d1ed8aa7014d9.jpg)  
**Text:** "a bicycle parked on a city street"  
**Confidence**: 0.616267969725777  
**Tags**: "outdoor" "building" "street" "truck" "bicycle" "parked" "city" "man" "carrying" "night" "cart" "sitting" "side" "riding" "light" "store" "motorcycle" "standing" "rain" "large" "water" "red" "rainy" "sign" "umbrella" "people"

* * *

![](http://cdn.sotong.io/insta/41f2c36b4a66125f3ef083bc5d0c7221.jpg)  
**Text:** "a group of people standing next to a train"  
**Confidence**: 0.6149708950308981  
**Tags**: "person" "indoor" "standing" "people" "table" "group" "man" "food" "small" "sitting" "train" "large" "filled" "woman" "red" "room" "many" "white" "display" "water" "holding" "playing" "crowd"

* * *

![](http://cdn.sotong.io/insta/13797bd85364b273ee0fa28811f8c935.jpg)  
**Text:** "a plate that has some food on a table"  
**Confidence**: 0.6139501484660129  
**Tags**: "food" "table" "plate" "indoor" "sitting" "fries" "meal" "sandwich" "filled" "white" "sauce" "cheese" "bowl" "banana" "meat" "fruit" "hot"

* * *

![](http://cdn.sotong.io/insta/e6727a5a057e60465e6b683305d8f076.jpg)  
**Text:** "the meal is prepared and ready to be eaten"  
**Confidence**: 0.6131074888276266  
**Tags**: "food" "table" "plate" "sitting" "meal" "container" "filled" "hot" "sauce" "cheese" "bowl" "dog" "side" "lunch" "wooden" "sandwich" "salad" "water" "soup"

* * *

![](http://cdn.sotong.io/insta/81febe7b2253f01c1c23d9c23f57b1f9.jpg)  
**Text:** "a group of people preparing food in a kitchen"  
**Confidence**: 0.61269247092412  
**Tags**: "indoor" "person" "table" "food" "kitchen" "counter" "cup" "man" "preparing" "window" "woman" "standing" "office" "sitting" "cooking" "desk" "filled" "plate" "people" "computer" "cake" "large" "cutting" "laptop" "restaurant" "sandwich" "group" "holding" "fruit" "hot" "sink" "phone"

* * *

![](http://cdn.sotong.io/insta/5dc88ec8f08ac73c6df1c4c1094ee842.jpg)  
**Text:** "a close up of a pizza on a plate"  
**Confidence**: 0.6122852029026341  
**Tags**: "custard" "food" "indoor" "plate" "sitting" "top" "cake" "table" "white" "piece" "sauce" "topped" "close" "covered" "cheese" "laying" "dish" "pizza"

* * *

![](http://cdn.sotong.io/insta/f5a3daa6254a899d71fc352dbd55a74b.jpg)  
**Text:** "a glass of beer"  
**Confidence**: 0.6099848995042969  
**Tags**: "table" "indoor" "cup" "sitting" "glass" "food" "filled" "large" "light" "laptop" "water" "top" "computer" "glasses" "standing" "tall" "room" "man" "night"

* * *

![](http://cdn.sotong.io/insta/1f580e14f31977edc7e7e54b60545d56.jpg)  
**Text:** "a plate of food with a sandwich and french fries"  
**Confidence**: 0.6099056922653705  
**Tags**: "food" "table" "plate" "fries" "indoor" "sitting" "tray" "hot" "side" "meal" "filled" "top" "dog" "half" "sandwich" "white" "bun" "bowl" "cheese"

* * *

![](http://cdn.sotong.io/insta/a2b77f78c27721ffa7830360aaa6039d.jpg)  
**Text:** "a boat in the water near a bridge"  
**Confidence**: 0.6090007109629412  
**Tags**: "outdoor" "water" "boat" "ship" "large" "river" "lake" "body" "sitting" "bridge" "city" "bench" "harbor" "dock" "old" "ocean" "docked" "white" "man"

* * *

![](http://cdn.sotong.io/insta/7e216243f26654e15b739643f6407e13.jpg)  
**Text:** "a bowl of soup on a white plate"  
**Confidence**: 0.6080411545202297  
**Tags**: "plate" "food" "table" "white" "sitting" "bowl" "top" "soup" "small" "filled" "sauce" "stew" "meat" "large" "sandwich" "toppings" "cheese"

* * *

![](http://cdn.sotong.io/insta/63251f210db474855fc7dc4919a3ecc8.jpg)  
**Text:** "a large brick building with a clock tower"  
**Confidence**: 0.6059549593234511  
**Tags**: "outdoor" "building" "clock" "tower" "top" "large" "brick" "sitting" "red" "brown" "old" "tall" "cloudy" "people" "white" "parked" "street" "standing" "blue" "field" "city" "flying"

* * *

![](http://cdn.sotong.io/insta/6f9cf26271a8875e814c4bc381b0385c.jpg)  
**Text:** "a close up of a plate of food and fruit"  
**Confidence**: 0.6056280542854336  
**Tags**: "food" "sashimi" "fruit" "filled" "piece" "cake" "slice" "dessert" "banana" "top" "car" "cream" "plate" "covered" "table" "sitting" "fresh" "plastic" "desert" "holding" "meat" "close" "bowl" "cheese" "toppings" "cut" "white"

* * *

![](http://cdn.sotong.io/insta/96559e338dfec52016e943c4a85cba73.jpg)  
**Text:** "a group of people standing in front of a building"  
**Confidence**: 0.6053085354063951  
**Tags**: "building" "outdoor" "city" "people" "street" "front" "small" "old" "boat" "large" "water" "group" "parked" "standing" "sitting" "bus" "green" "tall" "river" "top" "brick" "man" "table" "white" "bench" "woman" "tower" "clock" "train" "umbrella" "docked"

* * *

![](http://cdn.sotong.io/insta/c025f5b71357a77c21f1707d1481ba7d.jpg)  
**Text:** "a view of a living room with a large body of water"  
**Confidence**: 0.6029117177375951  
**Tags**: "water" "overlooking" "room" "window" "chair" "ocean" "view" "living" "building" "background" "table" "large" "body" "river" "city" "boat" "area" "glass" "furniture" "bridge" "parked"

* * *

![](http://cdn.sotong.io/insta/429595a1ef5b3a6215be4783cbe12a22.jpg)  
**Text:** "a view of a city skyline in the ocean"  
**Confidence**: 0.6014890845638724  
**Tags**: "outdoor" "water" "view" "ocean" "large" "city" "many" "full" "overlooking" "busy" "harbor" "filled" "lot" "people" "body" "blue"

* * *

![](http://cdn.sotong.io/insta/4ed63c558a873e5c5d0066584dee10c0.jpg)  
**Text:** "a living room with a large window"  
**Confidence**: 0.5998346153343007  
**Tags**: "window" "indoor" "room" "living" "building" "chair" "table" "view" "sitting" "overlooking" "large" "furniture" "ocean" "water" "city" "area" "television" "white" "door" "curtain"

* * *

![](http://cdn.sotong.io/insta/0ab80c61143a328647a2e584f5df9e8a.jpg)  
**Text:** "a ship is in the air"  
**Confidence**: 0.5987038559831475  
**Tags**: "outdoor" "water" "ship" "boat" "large" "top" "sitting" "view" "dock" "airplane" "docked" "blue" "city" "plane" "ocean" "body" "wooden" "air" "flying" "bird" "river" "bridge" "tall" "group" "tower"

* * *

![](http://cdn.sotong.io/insta/99575bbbfdaef46ac87a7c03d21ff58b.jpg)  
**Text:** "a piece of meat and vegetables"  
**Confidence**: 0.5935388910616889  
**Tags**: "food" "indoor" "piece" "slice" "sitting" "meat" "top" "cake" "black" "plate" "chocolate" "cut" "filled" "table" "close" "covered" "pan" "white" "broccoli" "laying"

* * *

![](http://cdn.sotong.io/insta/053b027500d276ce28193ebd4d02c828.jpg)  
**Text:** "a plate of food and a drink on a counter"  
**Confidence**: 0.5919825295404414  
**Tags**: "table" "food" "indoor" "plate" "counter" "kitchen" "sitting" "restaurant" "preparing" "man" "sandwich" "top" "filled" "large" "glasses" "glass" "woman" "bowl" "pizza" "standing" "holding" "white" "people"

* * *

![](http://cdn.sotong.io/insta/f5f98c38b133d6aefdf15ee9f12d1d23.jpg)  
**Text:** "a group of people standing on a dock near the water"  
**Confidence**: 0.5900855160747633  
**Tags**: "outdoor" "boat" "person" "water" "dock" "people" "standing" "pier" "group" "docked" "harbor" "lake" "parked" "body" "large" "man" "river" "park" "blue" "woman" "walking" "bridge" "white"

* * *

![](http://cdn.sotong.io/insta/7708ef15f8a2dccda7d950c698c81c45.jpg)  
**Text:** "a table with wine glasses"  
**Confidence**: 0.5883717682279584  
**Tags**: "indoor" "table" "wine" "glass" "window" "sitting" "room" "living" "filled" "glasses" "woman" "dining" "standing" "man" "red" "people" "large" "white" "kitchen" "group" "plate" "vase"

* * *

![](http://cdn.sotong.io/insta/ea990822c7060bb76910540dd02a843d.jpg)  
**Text:** "a large building in the city"  
**Confidence**: 0.5860886479584657  
**Tags**: "building" "outdoor" "street" "city" "town" "large" "walking" "tall" "light" "traffic" "train" "intersection" "red" "old" "people" "rain" "clock" "white" "track" "stop" "group" "standing" "hydrant" "parked" "road" "riding" "man"

* * *

![](http://cdn.sotong.io/insta/55088bb37fe53a9f2af85f81c1bf10d2.jpg)  
**Text:** "a table full of food sitting on a counter"  
**Confidence**: 0.5854034124497642  
**Tags**: "food" "table" "plate" "top" "sitting" "counter" "filled" "full" "kitchen" "large" "meat" "woman" "many" "cake" "standing" "rice" "water" "dog" "man"

* * *

![](http://cdn.sotong.io/insta/d2a4b76a4cb0fbb174223abbd3e4e399.jpg)  
**Text:** "a living room with blue walls"  
**Confidence**: 0.5843666441298326  
**Tags**: "building" "indoor" "room" "blue" "sitting" "small" "living" "table" "area" "green" "door" "furniture" "painted" "old" "white" "cat"

* * *

![](http://cdn.sotong.io/insta/5eb2ecad6155803be0531b39d7e74252.jpg)  
**Text:** "a sign hanging off the side of a building"  
**Confidence**: 0.5806857008128276  
**Tags**: "sign" "building" "photo" "sitting" "red" "street" "hanging" "stop" "white" "covered" "old" "man" "room" "traffic" "people"

* * *

![](http://cdn.sotong.io/insta/a72c1a10e6b3c97d25e9d076e8a64b9d.jpg)  
**Text:** "a room with a table and chairs"  
**Confidence**: 0.5801937209777366  
**Tags**: "indoor" "table" "chair" "room" "living" "area" "building" "sitting" "furniture" "filled" "large" "covered" "old" "fire" "city" "fireplace" "street" "white"

* * *

![](http://cdn.sotong.io/insta/691f1e06f1cf16e7f1efe27ac0fbe9ce.jpg)  
**Text:** "a picture of a shop"  
**Confidence**: 0.5788483261816019  
**Tags**: "building" "table" "chair" "area" "restaurant" "filled" "sign" "street" "city" "sitting" "people" "bar" "many" "store" "large" "light" "room" "group" "shop" "covered" "man" "night" "kitchen" "standing"

* * *

![](http://cdn.sotong.io/insta/3bb614fbe6060a609b87cfa4bb1004cd.jpg)  
**Text:** "a pan of food on a table"  
**Confidence**: 0.5786018069953394  
**Tags**: "food" "table" "cup" "plate" "sitting" "bread" "filled" "rice" "meat" "meal" "bowl" "tray" "cheese" "black" "full" "hot" "fruit" "pan" "wooden" "water" "cake" "pizza" "dog"

* * *

![](http://cdn.sotong.io/insta/158c2b7d7e8b0967cf37beb54d621b7f.jpg)  
**Text:** "a pizza sitting on a pan"  
**Confidence**: 0.5777197451716028  
**Tags**: "food" "indoor" "table" "sitting" "small" "top" "coffee" "plate" "paper" "sauce" "black" "bowl" "pizza" "doughnut" "cheese" "wooden" "donut" "sandwich" "pan" "laying"

* * *

![](http://cdn.sotong.io/insta/69f77def74b6c8d91e8e1d0d247fc76c.jpg)  
**Text:** "a graffiti covered wall"  
**Confidence**: 0.5755015747257323  
**Tags**: "fence" "outdoor" "photo" "building" "covered" "many" "street" "man" "city" "colorful" "wooden" "room" "young" "standing" "riding" "woman" "group" "sign" "graffiti" "white" "people"

* * *

![](http://cdn.sotong.io/insta/591470419a8a8f74835ae873f11f7056.jpg)  
**Text:** "a group of people standing in front of a television"  
**Confidence**: 0.5753997469632972  
**Tags**: "person" "indoor" "man" "front" "standing" "television" "holding" "room" "photo" "group" "people" "young" "woman" "posing" "living" "video" "wine" "wearing" "boy" "table" "playing" "large" "wii" "game"

* * *

![](http://cdn.sotong.io/insta/a5e92874e4048e5a12aaef858dfa28b4.jpg)  
**Text:** "a picture of a tree"  
**Confidence**: 0.5751846174778915  
**Tags**: "outdoor" "grass" "tree" "sitting" "palm" "green" "front" "traffic" "hanging" "food" "light" "sign" "pole" "street" "stop" "red" "group" "standing" "fire" "parked" "man"

* * *

![](http://cdn.sotong.io/insta/d340b13c868bd5a27a21c8acb1f1c5d6.jpg)  
**Text:** "a slice of pizza"  
**Confidence**: 0.5743009438969572  
**Tags**: "food" "sitting" "indoor" "table" "sandwich" "piece" "plate" "paper" "slice" "top" "small" "eaten" "pizza" "half" "chicken" "meat" "cheese" "sauce" "eating" "bun" "black" "holding" "toppings" "broccoli" "laying" "white" "lettuce"

* * *

![](http://cdn.sotong.io/insta/67fcce168e264e7dfb928d3b8f978782.jpg)  
**Text:** "a view of a city harbor"  
**Confidence**: 0.5739385865360995  
**Tags**: "outdoor" "building" "city" "large" "harbor" "filled" "view" "sitting" "many" "snow" "top" "lot" "cloudy" "plane" "clock" "water" "skiing" "boat" "airplane" "train" "tower" "riding" "standing" "track" "parked" "people" "white"

* * *

![](http://cdn.sotong.io/insta/609cfd48ea5942f9f6f02c62dad0f9ba.jpg)  
**Text:** "a ship is docked next to a large body of water"  
**Confidence**: 0.5714262615471967  
**Tags**: "outdoor" "water" "boat" "building" "ship" "large" "city" "bridge" "river" "body" "plane" "dock" "airplane" "harbor" "sitting" "top" "traveling" "docked" "ocean" "white" "train" "parked" "jet" "tower" "castle" "blue" "riding" "landing" "flying"

* * *

![](http://cdn.sotong.io/insta/f939eeb79e21949cacf4dd867cd0aa64.jpg)  
**Text:** "a display in a store"  
**Confidence**: 0.5698585113588145  
**Tags**: "building" "table" "food" "room" "sitting" "pizza" "covered" "colorful" "living" "filled" "many" "standing" "plate" "cake" "woman" "old" "large" "display" "man" "eating" "umbrella" "store" "people"

* * *

![](http://cdn.sotong.io/insta/fca170f44265404c0d960a9ea67e9d5c.jpg)  
**Text:** "a church with a large building"  
**Confidence**: 0.5666205469521013  
**Tags**: "outdoor" "building" "large" "old" "church" "tall" "front" "white" "tower" "sitting" "top" "clock" "table" "street" "yellow" "man" "red" "city" "people" "standing"

* * *

![](http://cdn.sotong.io/insta/44d7c0a75192a1c9810d4880f5f28df4.jpg)  
**Text:** "a cup sitting on a plate"  
**Confidence**: 0.5634880776339379  
**Tags**: "table" "plate" "cup" "indoor" "sitting" "food" "cake" "piece" "coffee" "glass" "bowl" "banana" "counter" "laying" "fruit" "white"

* * *

![](http://cdn.sotong.io/insta/7d4b2bfec481135bda9244e9b1dcae97.jpg)  
**Text:** "a large building"  
**Confidence**: 0.5632157673649015  
**Tags**: "building" "indoor" "cabinet" "kitchen" "sitting" "white" "large" "top" "black" "standing" "refrigerator" "wooden" "counter" "sign" "stove" "oven" "sink" "man"

* * *

![](http://cdn.sotong.io/insta/f37b4c3babf9a4401fefda7c85fe37c2.jpg)  
**Text:** "a pile of vegetables"  
**Confidence**: 0.5630762945517109  
**Tags**: "pile" "flower" "cabbage" "clothes" "bag" "covered" "full" "different" "filled" "peony" "bed" "white" "laying" "group"

* * *

![](http://cdn.sotong.io/insta/231c44f8657f4075723c461edd58b3af.jpg)  
**Text:** "a group of people walking in front of a building"  
**Confidence**: 0.562250430838998  
**Tags**: "building" "people" "walking" "group" "luggage" "area" "station" "large" "standing" "many" "filled" "train" "woman" "street" "several" "city" "riding" "suitcase" "platform" "table" "sign" "parked" "tall" "man" "clock"

* * *

![](http://cdn.sotong.io/insta/6a4f97f006f46e433e4804600ddfd4a1.jpg)  
**Text:** "a herd of sheep grazing on a lush green field"  
**Confidence**: 0.562146347251717  
**Tags**: "grass" "outdoor" "field" "sheep" "mountain" "nature" "large" "full" "hill" "grazing" "view" "green" "flying" "overlooking" "grassy" "pasture" "water" "many" "kite" "ocean" "people" "lot" "blue" "city" "group" "herd" "man"

* * *

![](http://cdn.sotong.io/insta/c8426b4e049756207d39a218f3aaefc1.jpg)  
**Text:** "a yellow car in a parking lot"  
**Confidence**: 0.5619106336205937  
**Tags**: "outdoor" "car" "yellow" "sitting" "parked" "city" "parking" "riding" "table" "lot" "track" "street" "standing" "man" "traffic" "motorcycle" "plane" "white"

* * *

![](http://cdn.sotong.io/insta/7ab89ce8dc7e15aafaa1bf282a396c67.jpg)  
**Text:** "a man standing on a sidewalk in front of a building"  
**Confidence**: 0.5608183621630431  
**Tags**: "outdoor" "building" "man" "person" "sidewalk" "standing" "street" "front" "walking" "park" "large" "city" "people" "clock" "tree" "holding" "woman" "riding" "young" "statue" "group" "dog" "hydrant" "white" "fire"

* * *

![](http://cdn.sotong.io/insta/0ad95407155de231ce5963ba2d5bbddd.jpg)  
**Text:** "a bicycle parked on the side of a building"  
**Confidence**: 0.5581059828083815  
**Tags**: "building" "outdoor" "sidewalk" "bicycle" "sitting" "parked" "street" "woman" "standing" "wooden" "red" "covered" "city" "train" "bench" "old" "food" "hydrant" "table" "snow" "pole" "man" "sign" "white" "group"

* * *

![](http://cdn.sotong.io/insta/8df579cdfc4af6a8f443e8bec1e8b495.jpg)  
**Text:** "a bowl of soup next to a glass of orange juice"  
**Confidence**: 0.5514220243733197  
**Tags**: "cup" "table" "food" "drink" "glass" "sitting" "coffee" "plate" "bowl" "top" "filled" "red" "soup" "phone" "orange" "counter" "fruit" "hot" "sandwich" "restaurant" "woman" "white"

* * *

![](http://cdn.sotong.io/insta/f53ddd9cb8b34bb06d4772b5ff36e66e.jpg)  
**Text:** "a blender filled with coffee and a glass of orange juice"  
**Confidence**: 0.5503181700593001  
**Tags**: "cup" "table" "glass" "food" "drink" "coffee" "ice" "sitting" "filled" "banana" "doughnut" "donut" "fruit" "full" "plate" "blender" "half" "beer" "sandwich" "pitcher" "top" "orange" "oranges" "wooden" "hot" "water" "phone" "tall" "white"

* * *

![](http://cdn.sotong.io/insta/4a32092a5b803af81b0b8647d332833b.jpg)  
**Text:** "a group of people riding motorcycles on a city street"  
**Confidence**: 0.5485445445554382  
**Tags**: "outdoor" "road" "building" "street" "people" "motorcycle" "riding" "sidewalk" "city" "busy" "man" "driving" "large" "traffic" "woman" "walking" "parked" "standing" "group" "intersection" "bus"

* * *

![](http://cdn.sotong.io/insta/a962fe7883e1bb1107dacd88675680f7.jpg)  
**Text:** "a boat is docked next to a large body of water"  
**Confidence**: 0.5476997527055547  
**Tags**: "water" "outdoor" "boat" "large" "sitting" "body" "building" "pier" "city" "harbor" "view" "filled" "lake" "overlooking" "bridge" "docked" "dock" "river" "bird" "many" "standing" "bench" "group" "white"

* * *

![](http://cdn.sotong.io/insta/1bb33bcda1dd036659a07ed1c47b75c6.jpg)  
**Text:** "a group of people standing outside of a building"  
**Confidence**: 0.5432115562174703  
**Tags**: "outdoor" "building" "people" "street" "sitting" "front" "green" "standing" "large" "walking" "sign" "man" "group" "city" "snow" "woman" "table" "covered" "white" "parked" "holding"

* * *

![](http://cdn.sotong.io/insta/cc4333f1ecea627ef9892ffa14e58611.jpg)  
**Text:** "a large tall building with a sunset in the city"  
**Confidence**: 0.5416545019062786  
**Tags**: "outdoor" "building" "street" "city" "sunset" "background" "house" "cloudy" "front" "clouds" "large" "tall" "traffic" "sitting" "road" "sun" "red" "clock" "light" "sign" "brick" "walking" "tower" "stop" "yellow" "standing" "water" "parked" "train" "blue" "river"

* * *

![](http://cdn.sotong.io/insta/67904ed52bc92fb4257098e7348e0507.jpg)  
**Text:** "a plate of food with broccoli"  
**Confidence**: 0.5409735235900939  
**Tags**: "food" "plate" "sitting" "sauce" "meat" "filled" "white" "top" "side" "broccoli" "black" "covered" "hot" "fruit" "table"

* * *

![](http://cdn.sotong.io/insta/f202368a9a53d968fc3c4a58c3ca12c8.jpg)  
**Text:** "a bowl of soup and a sandwich"  
**Confidence**: 0.5396273339638341  
**Tags**: "food" "cup" "plate" "filled" "coffee" "sauce" "bowl" "table" "side" "dish" "sandwich" "banana" "fruit" "close" "brown" "white" "baked" "pile" "hot" "holding" "soup" "bun" "pasta"

* * *

![](http://cdn.sotong.io/insta/a457eb570122e558e9108758f732c567.jpg)  
**Text:** "a close up of a sandwich"  
**Confidence**: 0.5373224453357958  
**Tags**: "food" "piece" "cake" "top" "sitting" "table" "small" "slice" "half" "paper" "cut" "plastic" "sandwich" "eaten" "close" "plate" "fruit" "made" "meat" "clear" "holding" "laying" "white"

* * *

![](http://cdn.sotong.io/insta/85d4b983d1149bcccf7dc9888cbe013c.jpg)  
**Text:** "a statue in front of a building"  
**Confidence**: 0.5360569222655547  
**Tags**: "outdoor" "building" "front" "house" "large" "clock" "flower" "sitting" "tall" "old" "church" "stone" "statue" "top" "tower" "white" "garden" "standing" "bench" "parked" "street" "walking" "sign" "city"

* * *

![](http://cdn.sotong.io/insta/df0b612449db93ee37501b6c7441278d.jpg)  
**Text:** "a clock tower in front of a building"  
**Confidence**: 0.530279261410998  
**Tags**: "outdoor" "building" "road" "street" "city" "front" "large" "clock" "people" "church" "old" "tall" "bus" "standing" "driving" "parked" "walking" "riding" "top" "decker" "group" "busy" "red" "double" "yellow" "tower" "train" "traffic" "white" "carriage" "horse" "man" "sign" "field"

* * *

![](http://cdn.sotong.io/insta/160278d2af4b073643c5c67c656afc0a.jpg)  
**Text:** "a flower arrangement in front of a building"  
**Confidence**: 0.5278564298533488  
**Tags**: "building" "outdoor" "road" "front" "large" "clock" "church" "tower" "street" "stone" "white" "parked" "flower" "old" "top" "tall" "city" "riding" "people" "walking" "snow" "standing" "fire" "garden"

* * *

![](http://cdn.sotong.io/insta/01403dbc1129fd87995e9e38ccf7a912.jpg)  
**Text:** "a large body of water with a city in the background"  
**Confidence**: 0.5267295658575463  
**Tags**: "outdoor" "water" "grass" "lake" "river" "building" "large" "small" "front" "sitting" "city" "green" "body" "cloudy" "boat" "eating" "park" "train" "standing" "man" "field" "red" "grassy" "tall" "people" "parked" "bridge" "group" "bus" "flying" "ocean"

* * *

![](http://cdn.sotong.io/insta/8643449d7b737f58a96b97e63dd8969a.jpg)  
**Text:** "a group of children posing for a picture"  
**Confidence**: 0.525279892513743  
**Tags**: "person" "posing" "indoor" "wearing" "photo" "standing" "man" "holding" "group" "yellow" "black" "sitting" "skiing" "dressed" "brown" "young" "row" "girl" "large" "colorful" "white" "woman" "red" "room"

* * *

![](http://cdn.sotong.io/insta/187aded851b8cf3a981890ae44aad82d.jpg)  
**Text:** "a group of people standing in front of a building"  
**Confidence**: 0.5200539663923939  
**Tags**: "building" "outdoor" "monastery" "front" "people" "large" "walking" "standing" "group" "clock" "city" "sitting" "old" "stone" "top" "man" "riding" "parked" "woman" "street" "kite" "playing" "young" "tower" "flying"

* * *

![](http://cdn.sotong.io/insta/62b08d8cfa71f90a884c374afd75e07e.jpg)  
**Text:** "a large white building"  
**Confidence**: 0.5189420844498063  
**Tags**: "building" "outdoor" "mosque" "water" "large" "front" "standing" "white" "sitting" "top" "man" "boat" "old" "riding" "sheep" "field" "group" "people"

* * *

![](http://cdn.sotong.io/insta/9ca2d2e1bd926be50004da29ad7c3c3e.jpg)  
**Text:** "a bird is sitting on a table"  
**Confidence**: 0.5159583488550623  
**Tags**: "table" "bird" "water" "small" "sitting" "dog" "food" "man" "green" "standing" "computer" "holding" "woman" "laying" "white" "room" "group"

* * *

![](http://cdn.sotong.io/insta/3fdba461571d2c61a724e1bde0eee4e7.jpg)  
**Text:** "a large tall building with palm trees"  
**Confidence**: 0.5151314048477378  
**Tags**: "outdoor" "building" "tall" "palm" "street" "city" "background" "front" "standing" "side" "tower" "large" "traffic" "sign" "clock" "man" "stop" "intersection" "red" "bird" "snow" "riding" "flying" "blue" "white"

* * *

![](http://cdn.sotong.io/insta/26e3a1ce2673c7c2e092b333c49b547b.jpg)  
**Text:** "a group of people standing in a room"  
**Confidence**: 0.5132845706447771  
**Tags**: "ceiling" "indoor" "person" "table" "sitting" "room" "man" "box" "people" "standing" "large" "area" "computer" "woman" "laptop" "yellow" "luggage" "display" "living" "young" "television" "group"

* * *

![](http://cdn.sotong.io/insta/0f667d1bfc0b640fdaf8ea468672d888.jpg)  
**Text:** "a blender filled with coffee and a glass of beer"  
**Confidence**: 0.5088928171247402  
**Tags**: "cup" "table" "food" "drink" "sitting" "glass" "coffee" "filled" "ice" "beer" "doughnut" "donut" "dog" "orange" "red" "hot" "sandwich" "water" "blender" "laying"

* * *

![](http://cdn.sotong.io/insta/a79dc5c7ca1b2225ded24ca6c2406bd9.jpg)  
**Text:** "there is a large window"  
**Confidence**: 0.5084073770928735  
**Tags**: "building" "indoor" "window" "sitting" "table" "wooden" "door" "top" "black" "standing" "room" "white" "water" "large" "bench" "clock" "cat"

* * *

![](http://cdn.sotong.io/insta/e528451e44f8bc62b4f61da6083649e9.jpg)  
**Text:** "a blender filled with coffee on the table"  
**Confidence**: 0.5056999644702691  
**Tags**: "cup" "table" "indoor" "coffee" "drink" "sitting" "food" "glass" "plate" "counter" "top" "topped" "filled" "glasses" "beer" "pitcher" "wooden" "water" "kitchen" "blender" "hot"

* * *

![](http://cdn.sotong.io/insta/e5347f707553af4e1de0fdf1a78e4903.jpg)  
**Text:** "a sign in front of a store"  
**Confidence**: 0.5029527298537492  
**Tags**: "building" "outdoor" "sign" "front" "sitting" "yellow" "restaurant" "table" "standing" "store" "woman" "large" "people" "parked" "street"

* * *

![](http://cdn.sotong.io/insta/4da56f41966ec10e8dffb4ae72b181e6.jpg)  
**Text:** "a group of people walking down a street next to tall buildings"  
**Confidence**: 0.5027864412870565  
**Tags**: "building" "outdoor" "street" "city" "walking" "people" "sidewalk" "busy" "group" "standing" "sign" "traffic" "large" "tall" "man" "green" "bus" "woman" "road" "riding" "store" "train"

* * *

![](http://cdn.sotong.io/insta/f7607acd140089139910621b3cab3990.jpg)  
**Text:** "a castle with a house in the water"  
**Confidence**: 0.5027042029001095  
**Tags**: "outdoor" "water" "building" "house" "large" "castle" "grass" "top" "small" "sitting" "horse" "lake" "grazing" "white" "river" "city" "clock" "standing" "boat" "man" "people" "riding" "tall"

* * *

![](http://cdn.sotong.io/insta/d039ef712fcf759b7ec31a6f3e3d2960.jpg)  
**Text:** "many colorful umbrellas"  
**Confidence**: 0.502013112083434  
**Tags**: "colorful" "table" "items" "different" "many" "colored" "sitting" "green" "little" "colors" "birthday" "old" "holding" "bird" "covered" "cake" "woman" "young" "computer" "game" "plate" "blue" "man" "playing" "group" "clock" "laying" "standing" "umbrella"

* * *

![](http://cdn.sotong.io/insta/3ceeccd97c4449f91c1d33561c714b25.jpg)  
**Text:** "a path next to a stone wall"  
**Confidence**: 0.5016460356464207  
**Tags**: "outdoor" "stone" "building" "path" "rock" "grass" "brick" "dirt" "narrow" "large" "small" "sitting" "side" "water" "trail" "river" "park" "bench" "walking" "bushes" "old" "standing" "forest" "garden" "street" "bridge"

* * *

![](http://cdn.sotong.io/insta/5aaecfe808e6ba3982e71b5b8ad7d3e6.jpg)  
**Text:** "a close up of a tray of donuts"  
**Confidence**: 0.49836052071287623  
**Tags**: "indoor" "food" "large" "half" "cut" "board" "tray" "sliced" "shaped" "ready" "chocolate" "topped" "made" "top" "cutting" "pan" "decorated" "close" "pepperoni" "sitting" "grill" "covered" "oven" "baked" "green" "several" "knife" "many" "plate" "cooking" "group" "cake"

* * *

![](http://cdn.sotong.io/insta/96370f7b662b2825c1a0a98984eaad14.jpg)  
**Text:** "a street filled with lots of traffic"  
**Confidence**: 0.4966759743066465  
**Tags**: "outdoor" "car" "road" "street" "bunch" "walking" "filled" "busy" "city" "lot" "riding" "group" "many" "man" "several" "people" "traffic" "driving" "parked" "umbrella" "woman" "standing" "large" "parking" "holding" "sign"

* * *

![](http://cdn.sotong.io/insta/1dc0ca80059d80c632466d6b42a185d9.jpg)  
**Text:** "a group of people standing in front of a body of water"  
**Confidence**: 0.496605697022707  
**Tags**: "outdoor" "water" "mountain" "grass" "background" "people" "lake" "sitting" "group" "front" "large" "green" "body" "boat" "ocean" "standing" "river" "walking" "riding" "flying" "tree" "man" "beach" "parked" "wave"

* * *

![](http://cdn.sotong.io/insta/9d888e82c4db051d9936476f047e5c8d.jpg)  
**Text:** "a city at night"  
**Confidence**: 0.4961027638686413  
**Tags**: "light" "building" "city" "filled" "traffic" "top" "table" "standing" "tower" "street" "night"

* * *

![](http://cdn.sotong.io/insta/d9fc9cf18b5fd111a2140631a086400c.jpg)  
**Text:** "a dining room table with a bicycle"  
**Confidence**: 0.4958517267784334  
**Tags**: "indoor" "bicycle" "chair" "table" "room" "yellow" "kitchen" "red" "dining" "wooden" "sitting" "black" "standing" "door" "old" "living" "bedroom"

* * *

![](http://cdn.sotong.io/insta/a50b801196a8bd36246e303471118beb.jpg)  
**Text:** "a large stone building with a clock on the side of a road"  
**Confidence**: 0.4918458370838488  
**Tags**: "outdoor" "building" "road" "street" "sidewalk" "parked" "front" "clock" "sitting" "walking" "town" "city" "old" "large" "stone" "church" "man" "riding" "side" "people" "bench" "tower" "standing" "woman" "brick" "stop" "park" "statue" "red" "hydrant" "fire" "group" "sign" "white"

* * *

![](http://cdn.sotong.io/insta/a7146f8dc4d583dff0c374f87e078a29.jpg)  
**Text:** "a plate of food and a bottle of beer"  
**Confidence**: 0.49007327827785296  
**Tags**: "table" "food" "cup" "sitting" "bottle" "plate" "top" "glass" "counter" "filled" "wooden" "beer" "meat" "large" "snow" "kitchen"

* * *

![](http://cdn.sotong.io/insta/7bfa60bad37ed9a284d97f5a1416cc05.jpg)  
**Text:** "a picture of a large city"  
**Confidence**: 0.4889015647889446  
**Tags**: "outdoor" "building" "city" "large" "boat" "front" "water" "light" "sitting" "filled" "top" "standing" "street" "clock" "red" "traffic" "riding" "snow"

* * *

![](http://cdn.sotong.io/insta/e78953f1798626b31af3da63fce29808.jpg)  
**Text:** "a group of people standing in front of a bridge"  
**Confidence**: 0.48856642056651683  
**Tags**: "outdoor" "person" "people" "fence" "building" "group" "bench" "standing" "water" "table" "man" "front" "sitting" "park" "large" "overlooking" "airplane" "walking" "woman" "river" "bridge" "city" "white" "plane" "boat" "jet" "crowd" "board" "street" "clock" "train" "ocean" "parked" "court"

* * *

![](http://cdn.sotong.io/insta/9a39db791be8924b84009fe2fd08f623.jpg)  
**Text:** "a display in a store"  
**Confidence**: 0.4875513699587164  
**Tags**: "black" "store" "food" "display" "clock" "train"

* * *

![](http://cdn.sotong.io/insta/cd47676aadd3482fc46f07d09981a73c.jpg)  
**Text:** "a tray of food and a glass of wine"  
**Confidence**: 0.4847602761850267  
**Tags**: "table" "cup" "food" "plate" "glass" "sitting" "filled" "doughnut" "top" "tray" "bowl" "full" "counter" "water" "donut" "covered" "cake" "white" "sandwich" "coffee"

* * *

![](http://cdn.sotong.io/insta/a992f57ef58903ec4f35a363c42638fb.jpg)  
**Text:** "a group of people riding skis on top of a building"  
**Confidence**: 0.484380892556926  
**Tags**: "outdoor" "building" "people" "group" "snow" "skiing" "front" "walking" "standing" "riding" "covered" "area" "man" "city" "large" "parked" "many" "sign" "street" "table" "park" "slope" "bench" "young" "board" "motorcycle" "red" "road"

* * *

![](http://cdn.sotong.io/insta/cdd0cee6cf6499f1011a7a56e73e5619.jpg)  
**Text:** "a store front"  
**Confidence**: 0.48168060223201636  
**Tags**: "building" "many" "table" "street" "covered" "sitting" "city" "different" "bunch" "fire" "several" "group" "room" "man" "store" "parked"

* * *

![](http://cdn.sotong.io/insta/a624f090b0143370cfcff95509575670.jpg)  
**Text:** "a sign in front of a building"  
**Confidence**: 0.4807278157986823  
**Tags**: "building" "outdoor" "sign" "front" "street" "man" "fence" "sitting" "old" "traffic" "side" "stone" "stop" "board" "bench" "large" "walking" "red" "woman" "pole" "holding" "graffiti" "city" "riding" "standing" "hydrant" "train" "white"

* * *

![](http://cdn.sotong.io/insta/656c49314354bf30ea1675e9c958d222.jpg)  
**Text:** "a street sign with a building in the rain"  
**Confidence**: 0.48019274361525066  
**Tags**: "building" "outdoor" "sign" "street" "walking" "rain" "standing" "city" "brick" "people" "umbrella" "holding" "white" "traffic" "group" "room"

* * *

![](http://cdn.sotong.io/insta/d6184d7c1b4e5f0f931e23aeb4f427b0.jpg)  
**Text:** "a piece of meat and vegetables"  
**Confidence**: 0.4789051086153745  
**Tags**: "food" "sitting" "piece" "red" "covered" "top" "meat" "plate" "table" "hot" "snow"

* * *

![](http://cdn.sotong.io/insta/8693ce3d2962d48202e8be8d4a885d9c.jpg)  
**Text:** "a view of a bridge"  
**Confidence**: 0.47357628212550507  
**Tags**: "outdoor" "building" "water" "boat" "bridge" "view" "river" "body" "lake" "overlooking" "ship" "large" "seen" "mountain" "city" "ocean" "train" "close" "pole" "top" "track" "sun" "old" "sunset" "standing" "riding" "street" "docked" "tall" "tower" "group" "airplane" "plane" "traffic" "white"

* * *

![](http://cdn.sotong.io/insta/fe2f7b21988b2654503459dd6aa92347.jpg)  
**Text:** "a sign hanging from a tree"  
**Confidence**: 0.4713416418856867  
**Tags**: "outdoor" "plant" "building" "tree" "large" "sitting" "top" "sign" "tall" "tower" "palm" "park" "clock" "hanging" "plane" "white" "red" "blue" "standing"

* * *

![](http://cdn.sotong.io/insta/377e4c0858951c64e732e36e98cbd06f.jpg)  
**Text:** "a large elephant standing next to a tree"  
**Confidence**: 0.4707253659241434  
**Tags**: "outdoor" "reptile" "standing" "rock" "elephant" "tree" "large" "forest" "trunk" "zoo" "bird" "eating" "field" "enclosure" "giraffe"

* * *

![](http://cdn.sotong.io/insta/b1da7aa5e676e53a66dc3855b49c8f1f.jpg)  
**Text:** "a plane is flying over some clouds"  
**Confidence**: 0.4661402558887614  
**Tags**: "outdoor" "plane" "clouds" "airplane" "flying" "cloudy" "large" "view" "top" "air" "blue" "snow" "field" "sky" "white" "standing" "jet" "man" "hill" "dog" "people" "group" "skiing" "kite"

* * *

![](http://cdn.sotong.io/insta/1330aa6df9207b6d3036fae508eecfe0.jpg)  
**Text:** "a bowl of rice and vegetables"  
**Confidence**: 0.4616144120361148  
**Tags**: "food" "plate" "table" "rice" "meat" "filled" "sitting" "side" "bowl" "top" "white" "hot" "broccoli" "soup"

* * *

![](http://cdn.sotong.io/insta/26ccb2053b818d810718ec546d1fefbe.jpg)  
**Text:** "a group of people standing outside of a store"  
**Confidence**: 0.4612895906113246  
**Tags**: "building" "outdoor" "street" "sign" "sitting" "front" "city" "standing" "people" "corner" "group" "large" "train" "parked" "pole" "walking" "restaurant" "stop" "hydrant" "man" "tall" "store" "riding" "bus" "umbrella"

* * *

![](http://cdn.sotong.io/insta/0e21b82b58e3d946f32a8537247fd41d.jpg)  
**Text:** "a view of a city with a mountain in the background"  
**Confidence**: 0.46061976523306175  
**Tags**: "mountain" "outdoor" "building" "city" "view" "large" "town" "lot" "filled" "background" "hill" "many" "busy" "full" "harbor" "water" "ocean" "high" "crowded" "bus" "highway" "parking" "field" "people" "train" "parked" "traffic" "skiing" "riding" "tower" "beach" "white"

* * *

![](http://cdn.sotong.io/insta/3e8fe3a0d281be127f825cbb03738650.jpg)  
**Text:** "two hot dogs covered in sauce"  
**Confidence**: 0.45979828053276495  
**Tags**: "food" "indoor" "table" "sitting" "plate" "sauce" "covered" "red" "meat" "top" "sandwich" "hot" "snow" "chocolate" "cake" "water" "large" "white" "cheese" "dog" "bun" "man" "stuffed" "hotdog"

* * *

![](http://cdn.sotong.io/insta/2dbafdf267634b95f652f33512b76723.jpg)  
**Text:** "a church building"  
**Confidence**: 0.45839644751661784  
**Tags**: "building" "outdoor" "front" "large" "sitting" "church" "big" "white" "tall" "table" "standing" "man" "clock" "side" "doorway" "door" "parked" "train" "room" "snow" "riding" "double"

* * *

![](http://cdn.sotong.io/insta/34ffbf974e1fc90e5084afeda9996012.jpg)  
**Text:** "a box filled with different types of fruit"  
**Confidence**: 0.45769593090314575  
**Tags**: "table" "food" "box" "cake" "filled" "sitting" "different" "colorful" "fruit"

* * *

![](http://cdn.sotong.io/insta/4d1c390bf8d4ef1e5dcd4adc096fd63c.jpg)  
**Text:** "a group of people standing around a table with wine glasses"  
**Confidence**: 0.4559067876635998  
**Tags**: "indoor" "table" "person" "plate" "food" "woman" "wine" "glasses" "sitting" "standing" "people" "filled" "sink" "room" "group" "several" "mirror" "dining" "counter" "cake" "many" "man" "large" "restaurant" "bowl" "holding" "white" "kitchen" "red" "wedding"

* * *

![](http://cdn.sotong.io/insta/b89294b34524ecafa86ffdb674bf9109.jpg)  
**Text:** "a pan filled with food"  
**Confidence**: 0.4556542410273116  
**Tags**: "food" "indoor" "table" "sitting" "top" "filled" "piece" "black" "plate" "cheese" "pan" "meat" "wooden" "cake" "banana" "covered" "hot" "toppings" "soup" "pizza"

* * *

![](http://cdn.sotong.io/insta/5158e248bd3e9bce90502a80de5ad67e.jpg)  
**Text:** "a man sitting on a counter in a restaurant"  
**Confidence**: 0.4551030890503079  
**Tags**: "person" "man" "indoor" "table" "sitting" "people" "front" "food" "computer" "kitchen" "restaurant" "preparing" "standing" "counter" "woman" "desk" "large" "cooking" "young" "group" "holding" "room" "display" "playing" "pizza"

* * *

![](http://cdn.sotong.io/insta/8c7fd617890523d8ae2f910c2b8e8ceb.jpg)  
**Text:** "a train at night"  
**Confidence**: 0.45475662317457044  
**Tags**: "outdoor" "train" "track" "light" "large" "night" "city" "traffic" "clock" "sunset"

* * *

![](http://cdn.sotong.io/insta/af253b1d85f116b77e42cff893fb18cd.jpg)  
**Text:** "a group of people sitting at night"  
**Confidence**: 0.4541206192780775  
**Tags**: "person" "man" "purple" "water" "front" "table" "night" "standing" "sitting" "people" "large" "light" "sign" "lit" "river" "display" "group" "woman" "room" "bridge" "holding" "clock" "crowd" "umbrella" "white"

* * *

![](http://cdn.sotong.io/insta/1e06c2fefb950f2eb8d164bd4767ad3a.jpg)  
**Text:** "a large clock"  
**Confidence**: 0.45053306363928525  
**Tags**: "sitting" "building" "motorcycle" "large" "black" "old" "red" "top" "standing" "table" "track" "parked" "room" "clock" "brick" "city" "white" "tower" "street" "blue" "people" "man" "cat"

* * *

![](http://cdn.sotong.io/insta/418c0b7af0bc95f4c6c0442cae766088.jpg)  
**Text:** "a table topped with lots of counter space"  
**Confidence**: 0.44574803249293743  
**Tags**: "indoor" "table" "counter" "kitchen" "man" "sitting" "food" "top" "large" "standing" "wine" "bunch" "wooden" "hanging" "room" "computer" "white" "group" "snow"

* * *

![](http://cdn.sotong.io/insta/d24f801d2d94c2de0b0f54ad10fe07fe.jpg)  
**Text:** "a store filled with lots of windows"  
**Confidence**: 0.4457174300732644  
**Tags**: "indoor" "ceiling" "building" "metal" "filled" "large" "sitting" "room" "table" "sign" "standing" "store" "parked"

* * *

![](http://cdn.sotong.io/insta/093eb3e67f3eb4d3f3bc88c9096dddec.jpg)  
**Text:** "a group of people in a room"  
**Confidence**: 0.44545285372359905  
**Tags**: "indoor" "building" "person" "room" "table" "people" "large" "filled" "hall" "sitting" "glass" "library" "group" "many" "several" "living" "woman" "standing" "luggage" "man" "clock"

* * *

![](http://cdn.sotong.io/insta/1a970a3e7f6cbb1912706d2e1a9d32ce.jpg)  
**Text:** "a restaurant kitchen"  
**Confidence**: 0.4452404176501233  
**Tags**: "indoor" "building" "table" "room" "sitting" "kitchen" "white" "large" "living" "black" "clock" "old" "restaurant" "refrigerator" "standing"

* * *

![](http://cdn.sotong.io/insta/dbc241b826a2ab31ddbb91ebc4cfa310.jpg)  
**Text:** "a picture of a room"  
**Confidence**: 0.44462029969920425  
**Tags**: "food" "covered" "colorful" "room"

* * *

![](http://cdn.sotong.io/insta/204e11a925ea2e56d29b3f82f38c4373.jpg)  
**Text:** "a large tall building with a clock"  
**Confidence**: 0.4440807753490342  
**Tags**: "building" "outdoor" "large" "top" "front" "big" "tall" "sitting" "clock" "old" "giant" "city" "roof" "stone" "church" "tower" "white" "standing" "train" "blue"

* * *

![](http://cdn.sotong.io/insta/cd6171e80cba0afc1691f0c02ae5b994.jpg)  
**Text:** "a large tall building with a skyscraper in the background"  
**Confidence**: 0.443038677651647  
**Tags**: "outdoor" "building" "skyscraper" "city" "large" "tall" "top" "background" "front" "tower" "clock" "view" "blue" "flying" "white" "street" "standing" "air" "man"

* * *

![](http://cdn.sotong.io/insta/af5e50e1a26381c4e095d8445613782e.jpg)  
**Text:** "a tree sitting in a park"  
**Confidence**: 0.4422567569452269  
**Tags**: "grass" "outdoor" "plant" "park" "sitting" "tree" "bench" "green" "standing" "large" "grassy" "fire" "field" "white" "old" "garden" "hydrant" "tall" "street" "man"

* * *

![](http://cdn.sotong.io/insta/6be0e34a0320aa430f2be663a122bcae.jpg)  
**Text:** "a picture of a plane in the water"  
**Confidence**: 0.4391766844594973  
**Tags**: "outdoor" "water" "plane" "grass" "table" "sitting" "airplane" "large" "white" "top" "cloudy" "rain" "boat" "train" "snow" "air" "track"

* * *

![](http://cdn.sotong.io/insta/3924054e119aa7dbddfccff1e8a76be0.jpg)  
**Text:** "a store front"  
**Confidence**: 0.43849890449728113  
**Tags**: "indoor" "table" "sitting" "large" "filled" "front" "water" "row" "store" "group" "man" "standing" "people"

* * *

![](http://cdn.sotong.io/insta/e19e8e4e37881fac2f532b517de8b708.jpg)  
**Text:** "a view of a beach"  
**Confidence**: 0.43650941797235143  
**Tags**: "outdoor" "fence" "water" "building" "beach" "chair" "umbrella" "sitting" "ocean" "top" "table" "overlooking" "full" "boat" "many" "filled" "large" "harbor" "view" "lot" "body" "group" "red" "standing" "tower" "river" "people"

* * *

![](http://cdn.sotong.io/insta/11394fd701269a98781d377e197f7ed0.jpg)  
**Text:** "a building with snow on the ground"  
**Confidence**: 0.43618153511563856  
**Tags**: "snow" "outdoor" "building" "table" "sitting" "large" "top" "white" "covered" "cake" "man" "board" "riding" "standing"

* * *

![](http://cdn.sotong.io/insta/fe14c09f26fa4dbf54b17a3ab3e2d2d5.jpg)  
**Text:** "a hot dog and french fries on a plate"  
**Confidence**: 0.4342244525315323  
**Tags**: "fries" "food" "plate" "indoor" "dog" "sitting" "table" "hot" "pile" "close" "top" "white" "bun" "sandwich"

* * *

![](http://cdn.sotong.io/insta/df04f60f9738dccbd2f943114717abca.jpg)  
**Text:** "a carousel at night"  
**Confidence**: 0.4341281182552303  
**Tags**: "table" "light" "filled" "bunch" "many" "carousel" "lot" "large" "water" "night" "group" "standing" "city"

* * *

![](http://cdn.sotong.io/insta/caff87f423a9b77b3c612c8311ac83a5.jpg)  
**Text:** "a view of a city"  
**Confidence**: 0.43365840017378493  
**Tags**: "building" "outdoor" "city" "snow" "train" "track" "street" "traffic" "filled" "large" "many" "busy" "road" "parked" "group" "people" "standing" "bus"

* * *

![](http://cdn.sotong.io/insta/d62229348fe2bf16fd2f2a0b7fb0ec40.jpg)  
**Text:** "a view of a bridge"  
**Confidence**: 0.433089004270942  
**Tags**: "outdoor" "building" "bridge" "water" "view" "river" "large" "clock" "boat" "city" "sitting" "train" "street" "top" "body" "close" "pole" "tall" "tower" "window" "track" "standing" "fence"

* * *

![](http://cdn.sotong.io/insta/452996c077648611c2a5000035a3af43.jpg)  
**Text:** "a tree with snow on the ground next to a palm tree"  
**Confidence**: 0.4317821279596553  
**Tags**: "outdoor" "plant" "snow" "tree" "palm" "sitting" "standing" "shade" "area" "park" "covered" "top" "sandy" "water" "man" "large" "field" "people" "group" "bench" "forest" "beach" "hill" "herd" "skiing" "sign" "zebra" "clock" "slope" "riding" "tall" "street"

* * *

![](http://cdn.sotong.io/insta/7997dd533bc4e5da736a75ed128d1e48.jpg)  
**Text:** "a stone building"  
**Confidence**: 0.42870391460465096  
**Tags**: "building" "outdoor" "grass" "stone" "sitting" "brick" "covered" "large" "green" "bench" "flower" "park" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/34f2b03d05c853a1552bb3b49e0a14fa.jpg)  
**Text:** "a small dog"  
**Confidence**: 0.42713356708989114  
**Tags**: "dog" "outdoor" "mammal" "animal" "small" "black" "standing" "brown" "white" "sitting" "toy" "little" "bear" "cat" "top" "playing" "stuffed" "water"

* * *

![](http://cdn.sotong.io/insta/fdafebb88b73ddfdf29edd2a1e1cab97.jpg)  
**Text:** "a colorful kite"  
**Confidence**: 0.42515691100443836  
**Tags**: "grass" "table" "colorful" "cake" "kite" "umbrella"

* * *

![](http://cdn.sotong.io/insta/f8ec8f1e7fea64357980e8529be7c589.jpg)  
**Text:** "a view of a city bridge"  
**Confidence**: 0.4233917730505319  
**Tags**: "outdoor" "building" "fence" "water" "river" "bridge" "city" "large" "sitting" "boat" "front" "top" "riding" "view" "bench" "white" "standing" "train" "traveling" "red" "clock" "tall" "man" "sign" "bus" "people" "street"

* * *

![](http://cdn.sotong.io/insta/ad23ee983016ddc6d92f955228700d0f.jpg)  
**Text:** "a picture of some food"  
**Confidence**: 0.41961081223331137  
**Tags**: "food" "bread" "sitting" "filled" "top" "fruit" "banana" "cake" "table" "plate" "white" "covered"

* * *

![](http://cdn.sotong.io/insta/093482e9897eb80c66e7baa7c3d1c971.jpg)  
**Text:** "the tower of clouds in the dark"  
**Confidence**: 0.417518300347302  
**Tags**: "outdoor" "clouds" "smoke" "cloudy" "dark" "sunset" "sun" "front" "background" "large" "flying" "tower" "water" "red" "walking" "sky" "street" "city" "tree" "yellow" "standing" "airplane" "traffic" "river" "rain" "plane" "air" "sign"

* * *

![](http://cdn.sotong.io/insta/921452aa68f973fdbe77ff300b332bd5.jpg)  
**Text:** "a crowd of people standing on top of a building"  
**Confidence**: 0.4173086909427824  
**Tags**: "building" "outdoor" "people" "water" "city" "group" "large" "standing" "sitting" "bird" "table" "walking" "filled" "many" "bunch" "street" "woman" "holding" "crowd" "man" "boat" "dock" "umbrella" "rug" "parked" "river" "room" "tall"

* * *

![](http://cdn.sotong.io/insta/2dfdc484cfdad16ae82d89feaa2a8d3f.jpg)  
**Text:** "a red and yellow umbrella"  
**Confidence**: 0.4131713520026671  
**Tags**: "table" "umbrella" "red" "sitting" "hanging" "colorful" "yellow" "lamp" "top" "large" "standing" "laying" "room" "group" "people"

* * *

![](http://cdn.sotong.io/insta/2b326ff1243e77436808fa7f5b923b67.jpg)  
**Text:** "a tray of donuts"  
**Confidence**: 0.41309065133663114  
**Tags**: "food" "indoor" "top" "sitting" "doughnut" "table" "black" "small" "tray" "grill" "fruit" "topped" "counter" "filled" "pot" "cooking" "pan" "donut" "plate" "banana"

* * *

![](http://cdn.sotong.io/insta/b209bdcbe6172a384b3995b1195c1056.jpg)  
**Text:** "a group of people standing around a boat on the water"  
**Confidence**: 0.41295476665334585  
**Tags**: "outdoor" "water" "boat" "ship" "large" "people" "man" "standing" "giant" "top" "group" "holding" "skiing" "floating" "woman" "kite" "riding" "blue" "red"

* * *

![](http://cdn.sotong.io/insta/7c21af1309a0046176a7a3c74aa91aac.jpg)  
**Text:** "a bridge over a body of water"  
**Confidence**: 0.4125199369538491  
**Tags**: "bridge" "water" "outdoor" "building" "river" "boat" "view" "large" "traveling" "mountain" "train" "seen" "body" "going" "crossing" "lake" "track" "ocean" "clock"

* * *

![](http://cdn.sotong.io/insta/e4ab2fad37b836ab021bb392c2517620.jpg)  
**Text:** "a close up of a sandwich and a cup of coffee"  
**Confidence**: 0.40983598768518503  
**Tags**: "food" "custard" "cup" "table" "plate" "sitting" "top" "sauce" "filled" "close" "sandwich" "orange" "meat" "banana" "fruit" "hot" "laying"

* * *

![](http://cdn.sotong.io/insta/464a474d08a68167b8a78daedb4697d3.jpg)  
**Text:** "a store display window"  
**Confidence**: 0.409521165903575  
**Tags**: "window" "display" "store" "photo" "glass" "food" "different" "cake" "filled" "shop" "case" "standing" "table" "sign" "restaurant" "large" "wine" "man" "holding" "people" "street" "city"

* * *

![](http://cdn.sotong.io/insta/b781b1ea1202c9447ce5b98086ca4c05.jpg)  
**Text:** "a group of people standing outside of a restaurant"  
**Confidence**: 0.4077799079808629  
**Tags**: "building" "outdoor" "table" "people" "group" "standing" "food" "front" "man" "restaurant" "bunch" "street" "woman" "large" "store" "fire" "city" "sign" "train" "display"

* * *

![](http://cdn.sotong.io/insta/ac6945b4e4303fabd3477d89c74f96c3.jpg)  
**Text:** "a large tree"  
**Confidence**: 0.40596932277098896  
**Tags**: "outdoor" "hill" "tree" "large" "snow" "skiing" "covered" "green" "cloudy" "standing" "slope" "group" "riding" "air" "flying" "man" "field" "tall" "people" "white" "blue" "plane" "sheep"

* * *

![](http://cdn.sotong.io/insta/921afd57fc4209bf76789e92c5cdce06.jpg)  
**Text:** "a room with a couch and a table"  
**Confidence**: 0.4057783293351736  
**Tags**: "indoor" "table" "room" "sitting" "living" "computer" "furniture" "old" "desk" "white" "large" "man"

* * *

![](http://cdn.sotong.io/insta/14d89853339385c1dee72e0201ec4067.jpg)  
**Text:** "a view of a city with a mountain in the background"  
**Confidence**: 0.4037328564268265  
**Tags**: "mountain" "outdoor" "city" "background" "lot" "view" "hill" "filled" "large" "town" "ocean" "water" "overlooking" "full" "many" "body" "beach" "base" "busy" "field" "grazing" "group" "people" "highway" "riding" "parking" "traffic" "white" "tower" "bus" "slope" "air" "standing" "flying"

* * *

![](http://cdn.sotong.io/insta/df254a38dad4d186a03cd6fdc03b2b9e.jpg)  
**Text:** "a parking meter sitting next to a glass of orange juice"  
**Confidence**: 0.40258602001485627  
**Tags**: "cup" "orange" "outdoor" "bottle" "beverage" "glass" "table" "sitting" "food" "parking" "meter" "top" "yellow" "clear" "street" "side" "wine" "city" "red" "parked" "white" "snow" "drawn"

* * *

![](http://cdn.sotong.io/insta/c67cad642872f044b3522ff222e2d244.jpg)  
**Text:** "a statue of a tall building"  
**Confidence**: 0.40254495143404434  
**Tags**: "outdoor" "building" "sitting" "clock" "statue" "top" "large" "city" "sidewalk" "street" "woman" "tall" "standing" "man" "bus" "tower"

* * *

![](http://cdn.sotong.io/insta/f75c5d5f7fa99cf1207de8a32dd07aca.jpg)  
**Text:** "a city bridge"  
**Confidence**: 0.4019318754809334  
**Tags**: "building" "outdoor" "city" "fence" "bridge" "train" "water" "light" "filled" "bench" "large" "street" "riding" "green" "people" "traveling" "river" "traffic" "track" "driving" "woman" "standing" "bus" "road" "tall"

* * *

![](http://cdn.sotong.io/insta/861a7bdf168e1d4ec97adb41c6f579ab.jpg)  
**Text:** "a man preparing food in a store"  
**Confidence**: 0.4007788328016102  
**Tags**: "table" "person" "indoor" "food" "man" "sitting" "woman" "preparing" "standing" "kitchen" "front" "eating" "filled" "shop" "large" "young" "people" "cake" "plate" "counter" "store" "birthday" "restaurant" "group" "dog" "holding" "room" "sandwich" "display" "pizza"

* * *

![](http://cdn.sotong.io/insta/9463692c8fbcc4d62cd625379aae0218.jpg)  
**Text:** "a red and white chair sitting next to a dining room table"  
**Confidence**: 0.39958263281924444  
**Tags**: "table" "indoor" "chair" "sitting" "white" "red" "dining" "building" "small" "room" "black" "plate" "wooden" "bed" "kitchen"

* * *

![](http://cdn.sotong.io/insta/18cd2c9a97ee0dfef36aadcf92c10d86.jpg)  
**Text:** "a large crowd at night"  
**Confidence**: 0.3990473227382118  
**Tags**: "object" "light" "large" "table" "night" "covered" "decorated" "filled" "traffic" "lit" "street" "standing" "city" "crowd" "umbrella" "snow" "water" "red" "man" "white"

* * *

![](http://cdn.sotong.io/insta/9ff44cc3d72d833086c7e48d7ac681c5.jpg)  
**Text:** "a chair sitting next to a body of water"  
**Confidence**: 0.39342066771328355  
**Tags**: "water" "building" "table" "chair" "sitting" "harbor" "large" "empty" "ocean" "view" "room" "body" "boat" "living" "group" "white" "city" "umbrella"

* * *

![](http://cdn.sotong.io/insta/3d19bc3c747a1b613ad6dec0596455c7.jpg)  
**Text:** "there is a guitar"  
**Confidence**: 0.3923337812759503  
**Tags**: "indoor" "table" "sitting" "small" "guitar" "black" "top" "room" "holding" "man" "living"

* * *

![](http://cdn.sotong.io/insta/80c3b0cc70747e1955617ccf51a381ef.jpg)  
**Text:** "a bowl filled with bananas"  
**Confidence**: 0.3917552485675844  
**Tags**: "indoor" "food" "sitting" "banana" "filled" "wooden" "bowl" "table" "top" "black" "fruit" "plate" "pan" "brown"

* * *

![](http://cdn.sotong.io/insta/a0ae949da7eac582ebff1467e2e6fa34.jpg)  
**Text:** "a plate of food with a sandwich and french fries"  
**Confidence**: 0.3906410174295479  
**Tags**: "food" "plate" "table" "sitting" "cup" "fries" "meat" "white" "meal" "side" "sandwich" "hot" "bun" "sauce" "dog"

* * *

![](http://cdn.sotong.io/insta/415251b18bff81c71165ea6e439fd407.jpg)  
**Text:** "a crowd of people standing in a large city"  
**Confidence**: 0.38883799487317805  
**Tags**: "outdoor" "city" "building" "large" "people" "many" "filled" "crowd" "full" "standing" "view" "umbrella" "water" "group" "lot" "harbor" "busy" "traffic" "ocean" "herd" "man" "river" "field"

* * *

![](http://cdn.sotong.io/insta/39d247f2c2f935f0a68339b1468d4071.jpg)  
**Text:** "a tall building next to a tree"  
**Confidence**: 0.38427032187296656  
**Tags**: "outdoor" "building" "tall" "large" "flying" "front" "tree" "high" "tower" "blue" "standing" "sitting" "top" "clock" "green" "cloudy" "city" "hill" "street" "white" "air"

* * *

![](http://cdn.sotong.io/insta/742d580b44a6f5e2f4a7cc7f778f0262.jpg)  
**Text:** "a group of sheep"  
**Confidence**: 0.38229234972344667  
**Tags**: "outdoor" "group" "sheep" "standing" "photo" "white" "camera" "different" "young" "black" "field" "herd"

* * *

![](http://cdn.sotong.io/insta/3768d0ad9a76a97b7faaf76e6ed04b16.jpg)  
**Text:** "a red cup sitting on a plate"  
**Confidence**: 0.38213365968989266  
**Tags**: "cup" "table" "food" "coffee" "plate" "drink" "indoor" "dessert" "sitting" "red" "cream" "topped" "hot" "sauce" "orange" "white" "glass" "top" "fruit" "large" "cheese" "cake" "sandwich" "dog"

* * *

![](http://cdn.sotong.io/insta/c3e95d976e31ca183d36083d2d71eede.jpg)  
**Text:** "a tower that has a large body of water"  
**Confidence**: 0.38154591597327714  
**Tags**: "outdoor" "water" "building" "background" "grass" "large" "river" "city" "lake" "body" "overlooking" "view" "green" "tall" "top" "boat" "hill" "mountain" "bench" "tower" "blue" "ocean" "bridge" "white" "park" "field" "flying" "clear" "airplane"

* * *

![](http://cdn.sotong.io/insta/ce1b350be6621fff285a233661b0c764.jpg)  
**Text:** "a boat parked next to a palm tree"  
**Confidence**: 0.3809661268207261  
**Tags**: "outdoor" "water" "building" "boat" "house" "harbor" "resort" "table" "small" "large" "people" "sitting" "lake" "group" "lined" "palm" "traveling" "swimming" "floating" "umbrella" "parked" "river" "blue" "docked" "street" "tower"

* * *

![](http://cdn.sotong.io/insta/6325d8dd46a83bd804a0099239cc997a.jpg)  
**Text:** "a group of people laying on a dirt road"  
**Confidence**: 0.38090092748567117  
**Tags**: "outdoor" "water" "group" "people" "sitting" "standing" "walking" "man" "top" "several" "parked" "tree" "riding" "dirt" "large" "park" "boat" "laying" "river" "street" "motorcycle"

* * *

![](http://cdn.sotong.io/insta/00336bad2c2082b293f13bd07d074f80.jpg)  
**Text:** "a group of people standing outside of a shop"  
**Confidence**: 0.3805404733614252  
**Tags**: "building" "outdoor" "person" "street" "woman" "people" "shop" "sitting" "standing" "man" "many" "red" "walking" "city" "sign" "busy" "group" "store" "riding" "parked"

* * *

![](http://cdn.sotong.io/insta/e8581044bf4c67bd5e30b1ae21dff832.jpg)  
**Text:** "a group of people on a beach next to the ocean"  
**Confidence**: 0.3784029662066472  
**Tags**: "outdoor" "water" "beach" "umbrella" "chair" "ocean" "clouds" "cloudy" "group" "people" "sandy" "day" "sitting" "top" "standing" "sun" "large" "man"

* * *

![](http://cdn.sotong.io/insta/c8e6904d524588a77968bb5fc6b2fcd8.jpg)  
**Text:** "an umbrella hanging from a building"  
**Confidence**: 0.37830939542922837  
**Tags**: "building" "ride" "table" "sitting" "umbrella" "large" "top" "hanging" "store" "display" "black" "city" "clock" "standing" "night" "boat" "carousel" "street" "air" "room" "man"

* * *

![](http://cdn.sotong.io/insta/17dc05cc90603f2b3ecd8092fd0aa20f.jpg)  
**Text:** "a red light at night"  
**Confidence**: 0.3782151136211239  
**Tags**: "red" "bright" "sitting" "photo" "front" "light" "table" "standing" "old" "room" "train" "clock" "bus" "man" "night"

* * *

![](http://cdn.sotong.io/insta/cf2a22b51e4d33b0e40d588632e8b645.jpg)  
**Text:** "a fountain in the rain"  
**Confidence**: 0.3768266503482216  
**Tags**: "table" "building" "cake" "fountain" "water" "sitting" "light" "top" "food" "man" "large" "standing" "boat" "display" "group" "umbrella" "yellow" "rain" "white" "snow" "room"

* * *

![](http://cdn.sotong.io/insta/c804c233ac4c83c7f2721ef514ea398e.jpg)  
**Text:** "a bunch of bananas"  
**Confidence**: 0.37608016747604295  
**Tags**: "animal" "covered" "sitting" "old" "side" "large" "water" "lot" "many" "top" "table" "bunch" "street" "fire" "bird" "snow" "parking" "group" "river" "ocean" "field"

* * *

![](http://cdn.sotong.io/insta/d4b4e689ba587982a1153ab740c1280d.jpg)  
**Text:** "a view of a building"  
**Confidence**: 0.3726995694620604  
**Tags**: "building" "indoor" "window" "table" "view" "city" "sitting" "brick" "street" "walking" "light" "man" "woman" "large" "standing" "people" "holding" "red" "traffic" "white" "group" "room" "train"

* * *

![](http://cdn.sotong.io/insta/217e0983db6addabec206bef3492ccb5.jpg)  
**Text:** "a group of people standing in front of a building"  
**Confidence**: 0.37150972980683156  
**Tags**: "building" "outdoor" "person" "front" "standing" "light" "lit" "table" "decorated" "woman" "cake" "street" "people" "man" "colorful" "large" "sign" "walking" "holding" "city" "riding" "group" "traffic" "tall" "night"

* * *

![](http://cdn.sotong.io/insta/3786712d4fc023d05801932a5e9b9314.jpg)  
**Text:** "a plate of pasta with some soup"  
**Confidence**: 0.3663507991519769  
**Tags**: "food" "plate" "indoor" "table" "cup" "sitting" "white" "sauce" "soup" "bowl" "top" "meal" "pasta" "restaurant" "sandwich" "meat" "filled" "dish" "cheese" "red" "hot" "pizza"

* * *

![](http://cdn.sotong.io/insta/a2b05fee725cbdde3ae19449b0aef10a.jpg)  
**Text:** "a flock of birds flying over a beach"  
**Confidence**: 0.3655220482748942  
**Tags**: "outdoor" "water" "grass" "sheep" "standing" "flock" "field" "group" "beach" "large" "cloudy" "rain" "top" "ocean" "sky" "hill" "flying" "lot" "air" "body" "herd" "grazing" "sun" "sunset" "man" "bird" "people" "skiing" "city" "slope" "boat"

* * *

![](http://cdn.sotong.io/insta/2bff4da219871153fad40eef62fc41e6.jpg)  
**Text:** "a horse that is flying in the sky"  
**Confidence**: 0.3632511219246318  
**Tags**: "outdoor" "clouds" "cloudy" "standing" "top" "people" "large" "flying" "blue" "group" "air" "man" "hill" "street" "horse" "riding"

* * *

![](http://cdn.sotong.io/insta/92444e25dea56435539998aee41af492.jpg)  
**Text:** "a wooden table"  
**Confidence**: 0.3632221471915392  
**Tags**: "table" "indoor" "sitting" "desk" "small" "computer" "black" "counter" "food" "top" "kitchen" "red" "area" "room" "wooden" "keyboard" "water" "old" "bench" "laptop" "covered" "white" "plate" "snow"

* * *

![](http://cdn.sotong.io/insta/e36c86995778c782fc9681503de1188a.jpg)  
**Text:** "a long table sits in front of a building"  
**Confidence**: 0.36319165892950384  
**Tags**: "table" "indoor" "building" "water" "filled" "sitting" "long" "front" "several" "large" "room" "wooden" "people" "red" "group" "standing" "bench" "umbrella"

* * *

![](http://cdn.sotong.io/insta/3767e33cc4a610061f1f342baeb9745c.jpg)  
**Text:** "a sandwich with meat and vegetables"  
**Confidence**: 0.362636906067714  
**Tags**: "food" "table" "chocolate" "cake" "piece" "covered" "sitting" "different" "top" "filled" "plate" "sandwich" "donut" "large" "banana" "meat" "cut" "board" "white" "snow"

* * *

![](http://cdn.sotong.io/insta/5f86b8d33380e3e74e5a7b9082db8f4a.jpg)  
**Text:** "a harbor filled with lots of traffic"  
**Confidence**: 0.3564363399722336  
**Tags**: "outdoor" "building" "road" "street" "city" "bus" "car" "traffic" "large" "boat" "driving" "sitting" "harbor" "top" "water" "traveling" "red" "parked" "group" "riding" "white" "double" "decker" "man"

* * *

![](http://cdn.sotong.io/insta/844a1120000ea59ed80af98a81c3d7af.jpg)  
**Text:** "a group of people sitting on a dock near the water"  
**Confidence**: 0.3557273551661484  
**Tags**: "outdoor" "water" "sitting" "umbrella" "people" "table" "mountain" "chair" "boat" "group" "dock" "filled" "pier" "wooden" "beach" "standing" "man" "large" "body" "harbor" "many" "woman" "holding" "docked" "river"

* * *

![](http://cdn.sotong.io/insta/75877374925a51b1d543aa65c7118030.jpg)  
**Text:** "a street scene with focus on the side of a house"  
**Confidence**: 0.3504077695726143  
**Tags**: "outdoor" "road" "building" "street" "house" "small" "bus" "tree" "sidewalk" "city" "side" "riding" "sign" "red" "parked" "brick" "walking" "old" "stop" "white" "man" "motorcycle"

* * *

![](http://cdn.sotong.io/insta/a7557aa565ff264f6c449bc8b7159264.jpg)  
**Text:** "a group of men on a boat in a large city"  
**Confidence**: 0.34935114242916115  
**Tags**: "water" "outdoor" "boat" "city" "river" "building" "large" "ship" "body" "filled" "long" "view" "full" "bridge" "standing" "man" "many" "people" "old" "docked" "holding" "group"

* * *

![](http://cdn.sotong.io/insta/60a12e76b54fea2606a99365e5f4b404.jpg)  
**Text:** "a cup of coffee"  
**Confidence**: 0.34615307898740816  
**Tags**: "indoor" "table" "sitting" "counter" "front" "computer" "food" "laptop" "desk" "close" "glass" "white" "pizza" "red" "kitchen" "cup" "hydrant"

* * *

![](http://cdn.sotong.io/insta/f248e2c8885a6b1555d28ae14d3b9280.jpg)  
**Text:** "a large building"  
**Confidence**: 0.3431030520210114  
**Tags**: "outdoor" "building" "table" "sitting" "red" "front" "light" "street" "night" "standing" "man" "room" "bench" "city" "large" "old" "colorful" "fire" "water" "parked" "white" "motorcycle"

* * *

![](http://cdn.sotong.io/insta/33d5ec945af3f5c12b05b8ccf314101a.jpg)  
**Text:** "a large tall building with a mountain in the background"  
**Confidence**: 0.3405775621620313  
**Tags**: "outdoor" "building" "large" "sitting" "top" "water" "train" "green" "mountain" "tower" "tall" "boat" "city" "white" "clock" "air" "umbrella" "standing" "man" "flying" "field" "track"

* * *

![](http://cdn.sotong.io/insta/5555585aa115728514d5a0850c8c8da8.jpg)  
**Text:** "a silver car"  
**Confidence**: 0.3401332489309682  
**Tags**: "animal" "shellfish" "car" "black" "sitting" "food" "large" "table" "green" "plate" "silver" "motorcycle" "parked"

* * *

![](http://cdn.sotong.io/insta/1e591d616a93198c1d04630598578702.jpg)  
**Text:** "a city street"  
**Confidence**: 0.33976432515784116  
**Tags**: "fence" "building" "outdoor" "street" "standing" "water" "city" "top" "table" "man" "group" "walking" "bridge" "wooden" "large" "holding" "pole" "traffic" "woman" "parked" "white" "bus" "people" "snow" "riding" "boat" "sign"

* * *

![](http://cdn.sotong.io/insta/1115ce22a1083159e5dfd894eb226ca1.jpg)  
**Text:** "a bird that is hanging on a wire"  
**Confidence**: 0.33659710879291727  
**Tags**: "outdoor" "wire" "large" "hanging" "top" "plane" "airplane" "sitting" "bird" "blue" "pole" "flying" "air" "high" "street" "city" "group" "standing" "skiing" "boat" "red" "sign" "white" "perched"

* * *

![](http://cdn.sotong.io/insta/1848f7031cf85155b87d5f8aeb9628be.jpg)  
**Text:** "a bench in front of a tree"  
**Confidence**: 0.3364413089492729  
**Tags**: "outdoor" "building" "bench" "sitting" "park" "front" "street" "large" "view" "area" "tree" "forest" "green" "bushes" "table" "old" "standing" "water" "brick" "clock" "sign" "field" "red" "garden" "tall" "people" "dirt" "river" "city" "white"

* * *

![](http://cdn.sotong.io/insta/3101301350b1a9a2bd4cd505eb393a33.jpg)  
**Text:** "a kitchen filled with lots of windows"  
**Confidence**: 0.3354332506755637  
**Tags**: "indoor" "window" "table" "filled" "area" "room" "view" "kitchen" "restaurant" "many" "large" "food" "white" "living" "purple" "night"

* * *

![](http://cdn.sotong.io/insta/8c77112ae3818b284299a3a0867d7460.jpg)  
**Text:** "a pole with a building in the city"  
**Confidence**: 0.3337403153677033  
**Tags**: "outdoor" "building" "city" "traffic" "large" "tall" "street" "light" "top" "skyscraper" "bridge" "pole" "riding" "standing" "tower" "bus" "man" "train" "sign" "clock"

* * *

![](http://cdn.sotong.io/insta/f096f8be495ceca03dabc057181b228d.jpg)  
**Text:** "a red umbrella in front of a building"  
**Confidence**: 0.3332878215524809  
**Tags**: "building" "outdoor" "red" "table" "front" "sitting" "umbrella" "large" "top" "man" "white" "woman" "holding" "standing" "room" "group"

* * *

![](http://cdn.sotong.io/insta/fccb7ae3e4a56ec8a3b949839d3cdbbe.jpg)  
**Text:** "a large white airplane parked in front of a building"  
**Confidence**: 0.33317958129528347  
**Tags**: "grass" "building" "outdoor" "sitting" "front" "lawn" "white" "parked" "standing" "top" "large" "woman" "plane" "field" "table" "man" "airplane" "black" "old" "display" "grassy" "air" "people" "luggage" "bed" "group" "umbrella"

* * *

![](http://cdn.sotong.io/insta/c65667a7c5f8d5e75c6fd3b3be174e4d.jpg)  
**Text:** "a group of people flying kites in a garden"  
**Confidence**: 0.33241077654146844  
**Tags**: "outdoor" "grass" "building" "large" "people" "group" "standing" "tree" "field" "green" "park" "flying" "kite" "garden" "man" "red" "tower" "clock" "tall" "grassy" "water" "hill" "white" "city"

* * *

![](http://cdn.sotong.io/insta/82b2f136c5e57d570f5b4a193a1317d6.jpg)  
**Text:** "an old suitcase"  
**Confidence**: 0.330024585356445  
**Tags**: "indoor" "top" "sitting" "luggage" "suitcase" "table" "old" "box" "standing" "cat" "case" "laying" "man"

* * *

![](http://cdn.sotong.io/insta/cd1ef3a4ef1e66947ce29f28b503196c.jpg)  
**Text:** "a group of clouds"  
**Confidence**: 0.3287382547442414  
**Tags**: "outdoor" "clouds" "snow" "blue" "cloudy" "view" "flying" "plane" "mountain" "field" "top" "airplane" "white" "air" "hill" "large" "group" "people" "standing" "skiing" "covered"

* * *

![](http://cdn.sotong.io/insta/95b7061394e4a42757d810da31485550.jpg)  
**Text:** "a large hall"  
**Confidence**: 0.32784935599943527  
**Tags**: "indoor" "building" "large" "luggage" "hall" "train" "clock" "station" "sitting" "room" "people" "suitcase" "many" "table" "standing" "gold" "church" "white" "man"

* * *

![](http://cdn.sotong.io/insta/a2b7c48d7a25cd0d8b599d3df24666ca.jpg)  
**Text:** "a large room"  
**Confidence**: 0.3277337165681687  
**Tags**: "indoor" "building" "large" "table" "room" "sitting" "top" "clock" "many" "people" "living" "white" "standing" "train" "group"

* * *

![](http://cdn.sotong.io/insta/71ec64a1087087bc5960e39c6793cd34.jpg)  
**Text:** "a display in a building"  
**Confidence**: 0.32644814673774364  
**Tags**: "building" "indoor" "table" "room" "large" "display" "man" "glass" "hanging" "white" "store" "living" "window" "standing" "people"

* * *

![](http://cdn.sotong.io/insta/41274a420a6d06c863019e7a03435a7f.jpg)  
**Text:** "a group of people standing around each other"  
**Confidence**: 0.3250810295305758  
**Tags**: "person" "indoor" "man" "people" "group" "table" "food" "standing" "woman" "room" "red" "holding" "white" "stuffed" "train" "hat"

* * *

![](http://cdn.sotong.io/insta/50f604e9531f73f8747f8be21536e19b.jpg)  
**Text:** "a view of a busy city beach"  
**Confidence**: 0.3227585829200067  
**Tags**: "outdoor" "building" "city" "water" "large" "ocean" "view" "full" "overlooking" "mountain" "top" "many" "standing" "covered" "lot" "field" "hill" "slope" "beach" "busy" "herd" "people" "crowded" "crowd" "man" "blue" "snow" "grazing" "skiing" "sheep"

* * *

![](http://cdn.sotong.io/insta/91c971507a8b2ae713bad9c965142eb4.jpg)  
**Text:** "a large body of water near a bridge"  
**Confidence**: 0.32257739298106297  
**Tags**: "outdoor" "water" "pier" "sitting" "body" "harbor" "beach" "dock" "large" "track" "bench" "city" "bridge" "train" "ocean" "clock" "boat" "tower" "cloudy" "river" "parked" "snow" "group" "riding" "standing" "man"

* * *

![](http://cdn.sotong.io/insta/e1ac1335dd5ed3af3587b819a690711d.jpg)  
**Text:** "a group of people standing in a garden"  
**Confidence**: 0.3225143875979942  
**Tags**: "outdoor" "building" "sitting" "front" "bench" "man" "park" "bus" "table" "garden" "tree" "stone" "people" "top" "street" "parked" "woman" "walking" "group" "standing" "young" "sign" "large" "riding" "display" "hydrant" "city" "zoo"

* * *

![](http://cdn.sotong.io/insta/14efafec79175d0fa6a17716cb711767.jpg)  
**Text:** "a truck on a city street"  
**Confidence**: 0.3207098490885207  
**Tags**: "building" "road" "outdoor" "street" "sidewalk" "city" "truck" "walking" "car" "man" "large" "riding" "bus" "busy" "people" "parked" "driving" "snow" "traffic" "woman" "standing" "sign" "store" "luggage" "tall" "group" "hydrant"

* * *

![](http://cdn.sotong.io/insta/91b72a14d8405a7a839ab83f24e3424b.jpg)  
**Text:** "a flock of birds sitting on top of a beach"  
**Confidence**: 0.3192011110879532  
**Tags**: "outdoor" "sitting" "playing" "beach" "grass" "group" "people" "car" "different" "bird" "bunch" "many" "large" "lot" "sand" "eating" "ball" "several" "standing" "young" "game" "field" "flock" "woman" "umbrella" "water" "man" "blue" "cat" "laying" "white" "parked"

* * *

![](http://cdn.sotong.io/insta/b4e89778d3f9b017b847ce989ca15c48.jpg)  
**Text:** "a bowl of food on a chocolate cake"  
**Confidence**: 0.31721071865737516  
**Tags**: "food" "indoor" "table" "cream" "bowl" "piece" "sitting" "plate" "chocolate" "top" "cake" "banana" "sauce" "ice" "dessert" "filled" "paper" "slice" "close" "black" "desert" "hot" "pan" "meat"

* * *

![](http://cdn.sotong.io/insta/4c3bfd9b756913c21d6ced42227f04f3.jpg)  
**Text:** "an animal is standing in the dirt"  
**Confidence**: 0.31531773785415174  
**Tags**: "animal" "outdoor" "mammal" "standing" "grass" "small" "dirt" "field" "top" "white" "brown" "rocky" "green" "sheep"

* * *

![](http://cdn.sotong.io/insta/aeed1abcab2536aa38ca8d8fdd4c8731.jpg)  
**Text:** "a vase of flowers on a table"  
**Confidence**: 0.3143696645611482  
**Tags**: "indoor" "table" "room" "living" "building" "sitting" "area" "small" "filled" "large" "laptop" "water" "glass" "covered" "furniture" "red" "computer" "fire" "white" "vase" "sign"

* * *

![](http://cdn.sotong.io/insta/2e2a110940ca623b139b179a92a77f7e.jpg)  
**Text:** "a group of people sitting in a restaurant"  
**Confidence**: 0.31110273115598525  
**Tags**: "person" "table" "sitting" "man" "people" "front" "group" "woman" "dog" "standing" "room" "red" "light" "holding" "computer" "restaurant" "young"

* * *

![](http://cdn.sotong.io/insta/24d11b4a3c9bbdd06874af0558a16895.jpg)  
**Text:** "a crowd of people standing on top of a building"  
**Confidence**: 0.3053905017537974  
**Tags**: "building" "outdoor" "road" "people" "clock" "large" "street" "front" "tower" "lot" "old" "standing" "city" "bridge" "group" "green" "walking" "giant" "crowd" "tall" "riding" "display" "train" "white" "parked" "sign"

* * *

![](http://cdn.sotong.io/insta/ab82bc212e29fe0bf29f80553fb5e131.jpg)  
**Text:** "a vase of flowers on a table"  
**Confidence**: 0.3050238101049762  
**Tags**: "table" "window" "sitting" "chair" "decorated" "front" "cake" "food" "topped" "top" "flower" "old" "wooden" "large" "vase" "plate" "glass" "wine" "living" "red" "room" "standing" "white" "pizza"

* * *

![](http://cdn.sotong.io/insta/af4b7e4ae7886d28dfe019c08609fc3e.jpg)  
**Text:** "a glass of orange juice"  
**Confidence**: 0.3036107190489426  
**Tags**: "cup" "table" "sitting" "glass" "yellow" "orange" "food" "beer" "red" "water" "glasses" "dog" "white" "hydrant" "sandwich" "pizza"

* * *

![](http://cdn.sotong.io/insta/0f87a9ed4099584c8e2e142c4a07d9c7.jpg)  
**Text:** "a table topped with lots of glasses of wine"  
**Confidence**: 0.29997806522191744  
**Tags**: "table" "glasses" "sitting" "filled" "food" "topped" "wine" "top" "group" "man" "counter" "large" "woman" "many" "standing" "people" "water" "plate" "white" "kitchen"

* * *

![](http://cdn.sotong.io/insta/5b0895cf659ab58b178b7e4ee5bf2d51.jpg)  
**Text:** "a view of a bridge"  
**Confidence**: 0.29824016665591235  
**Tags**: "outdoor" "view" "water" "building" "top" "city" "sitting" "street" "hanging" "standing" "large" "close" "bridge" "ocean" "boat" "man" "white" "red" "sunset" "field" "sign" "tower" "bus" "train" "group"

* * *

![](http://cdn.sotong.io/insta/2f7c66901b79ab8e88c8102c5e52b7ff.jpg)  
**Text:** "a boat sitting on top of a table"  
**Confidence**: 0.2964656989673878  
**Tags**: "table" "indoor" "window" "sitting" "large" "food" "room" "filled" "man" "dog" "fire" "water" "living" "boat" "red" "standing"

* * *

![](http://cdn.sotong.io/insta/dbaa6aff869400a8c365587acf9cfb03.jpg)  
**Text:** "a bunch of hot dogs"  
**Confidence**: 0.29295013772079503  
**Tags**: "food" "table" "cake" "sitting" "top" "hot" "covered" "red" "filled" "plate" "wooden" "many" "large" "group"

* * *

![](http://cdn.sotong.io/insta/8bee069e1381b00476323c6928c2e3ae.jpg)  
**Text:** "a close up of a bottle"  
**Confidence**: 0.2927942351548403  
**Tags**: "outdoor" "bottle" "sitting" "beach" "can" "water" "top" "blue" "table" "close" "food" "holding" "sand" "red" "standing" "laying" "ocean" "umbrella" "white"

* * *

![](http://cdn.sotong.io/insta/fa889a786c032585fdefec6f9d1b466a.jpg)  
**Text:** "a clock tower in front of a building"  
**Confidence**: 0.28987305550124726  
**Tags**: "outdoor" "building" "clock" "tower" "large" "top" "front" "red" "sitting" "yellow" "side" "tall" "cloudy" "street" "city" "white" "standing" "blue" "brick" "sign"

* * *

![](http://cdn.sotong.io/insta/766fc7b13867df6a9cf41e495f353073.jpg)  
**Text:** "a view of a clock tower in the middle of a street"  
**Confidence**: 0.28767298008795467  
**Tags**: "outdoor" "road" "building" "street" "clock" "house" "tower" "large" "car" "church" "view" "city" "red" "traffic" "light" "tall" "green" "water" "sign"

* * *

![](http://cdn.sotong.io/insta/5516fa555799e61515a65a20392079b8.jpg)  
**Text:** "an umbrella hanging from a tree"  
**Confidence**: 0.28148689807677274  
**Tags**: "outdoor" "building" "street" "large" "front" "sitting" "clock" "top" "city" "tree" "tall" "hanging" "tower" "yellow" "pole" "standing" "umbrella" "palm" "white"

* * *

![](http://cdn.sotong.io/insta/56b8855cbd422ecba2a9f74f62500554.jpg)  
**Text:** "a group of people standing in front of a building"  
**Confidence**: 0.2813805191157295  
**Tags**: "indoor" "person" "building" "people" "front" "table" "sitting" "standing" "girl" "group" "kitchen" "man" "woman" "room" "red" "large" "wine" "train" "white" "young" "old" "living" "fire" "clock" "oven" "stove"

* * *

![](http://cdn.sotong.io/insta/8ec14bdc99fd2cdcc7aefcd270bfb6dd.jpg)  
**Text:** "the roof of a building"  
**Confidence**: 0.28127169496436544  
**Tags**: "building" "outdoor" "roof" "sitting" "table" "old" "large" "stone" "fire" "street" "bench" "man" "clock" "parked" "tower"

* * *

![](http://cdn.sotong.io/insta/51b9020139cceb49b3a57bb465668676.jpg)  
**Text:** "a large bridge"  
**Confidence**: 0.2803148043476718  
**Tags**: "outdoor" "building" "green" "water" "sitting" "large" "top" "bird" "boat" "truck" "city" "table" "river" "bridge" "parked" "dock" "docked" "white" "airplane" "plane"

* * *

![](http://cdn.sotong.io/insta/95296291a45e90748bb3cecae1015b2a.jpg)  
**Text:** "an old fashioned stove"  
**Confidence**: 0.2786877198957816  
**Tags**: "indoor" "table" "sitting" "small" "computer" "top" "desk" "book" "set" "laptop" "wooden" "kitchen" "room" "old" "filled" "stove" "black" "living" "standing" "remote" "display" "man" "bed"

* * *

![](http://cdn.sotong.io/insta/d058c9bcf100787dbba4f9a5f884f80a.jpg)  
**Text:** "a large cake"  
**Confidence**: 0.2775467897519287  
**Tags**: "table" "indoor" "large" "cake" "decorated" "sitting" "food" "covered" "various" "circuit" "different" "people" "plate" "birthday" "white" "group" "toppings"

* * *

![](http://cdn.sotong.io/insta/1ae74c252c9b5b6042c782951ba452fc.jpg)  
**Text:** "a piece of food"  
**Confidence**: 0.2774398737564047  
**Tags**: "food" "table" "cake" "piece" "plate" "photo" "small" "sitting" "top" "white" "dog" "cutting" "board" "holding" "laying" "pizza" "knife" "hot" "cheese" "man"

* * *

![](http://cdn.sotong.io/insta/001f67f0dc9fef9334ec100db85d5b6e.jpg)  
**Text:** "an old photo of a book"  
**Confidence**: 0.274167426060697  
**Tags**: "text" "book" "photo" "old"

* * *

![](http://cdn.sotong.io/insta/de8ebaee4a03a679afa629e36de73366.jpg)  
**Text:** "purple flowers are in a dark room"  
**Confidence**: 0.2733846029219727  
**Tags**: "light" "table" "dark" "lit" "night" "sitting" "fireworks" "decorated" "large" "colorful" "purple" "yellow" "white" "standing" "room"

* * *

![](http://cdn.sotong.io/insta/5a5f47c7dabebb98c0dc5923673f6622.jpg)  
**Text:** "a table topped with lots of windows"  
**Confidence**: 0.2715204050253912  
**Tags**: "window" "table" "building" "wine" "sitting" "area" "top" "glass" "old" "room" "green" "wooden" "kitchen" "computer" "large" "standing" "train" "red" "man" "track"

* * *

![](http://cdn.sotong.io/insta/d0b12d01e1b9a0be1b273fbff471838f.jpg)  
**Text:** "a view of a clock tower"  
**Confidence**: 0.2711040190950547  
**Tags**: "outdoor" "building" "water" "large" "clock" "tower" "sitting" "river" "top" "city" "boat" "cloudy" "view" "body" "sunset" "bridge" "tall"

* * *

![](http://cdn.sotong.io/insta/e2f120172158c7df7ce02cb117d322d8.jpg)  
**Text:** "a sign in front of a building"  
**Confidence**: 0.27025951684729255  
**Tags**: "building" "outdoor" "front" "house" "street" "sign" "small" "old" "sitting" "white" "restaurant" "brick" "large" "parked" "store" "red" "man" "standing"

* * *

![](http://cdn.sotong.io/insta/7113501a31c35324362ede8cb27dd6ce.jpg)  
**Text:** "a man standing on a dock near the water"  
**Confidence**: 0.2701170586450993  
**Tags**: "outdoor" "water" "standing" "boat" "large" "man" "food" "bridge" "harbor" "body" "group" "dock" "lake" "river" "white" "zebra" "people" "blue" "ocean"

* * *

![](http://cdn.sotong.io/insta/cab8d31ce639e7a5ebc67cfcf6e27d3b.jpg)  
**Text:** "a train that is lit up at night"  
**Confidence**: 0.2692701440034068  
**Tags**: "table" "fence" "indoor" "night" "building" "sitting" "rail" "lit" "light" "bar" "wooden" "platform" "train" "water" "bus" "standing" "riding" "man"

* * *

![](http://cdn.sotong.io/insta/daccfece669c0d374763437a550ff83c.jpg)  
**Text:** "a bowl filled with meat and vegetables"  
**Confidence**: 0.268696038849062  
**Tags**: "food" "bowl" "filled" "plate" "meat" "table" "full" "stew" "pan" "covered" "cooked" "rice" "cake" "soup" "white"

* * *

![](http://cdn.sotong.io/insta/2a5f2578aa7f5412240126b849e597ca.jpg)  
**Text:** "a bridge over water"  
**Confidence**: 0.2665256619309045  
**Tags**: "outdoor" "water" "building" "grass" "green" "large" "bridge" "sitting" "front" "standing" "top" "flower" "lake" "park" "river" "white" "bench" "people" "tower" "boat" "field" "man" "group" "parked" "garden" "clock" "tall"

* * *

![](http://cdn.sotong.io/insta/815fcb7c09bdd8108c87e5863454a55d.jpg)  
**Text:** "a close up of food on a pan"  
**Confidence**: 0.26568152822213303  
**Tags**: "food" "sitting" "meat" "top" "sauce" "covered" "plate" "cheese" "filled" "close" "table" "toppings" "white" "pan" "laying"

* * *

![](http://cdn.sotong.io/insta/9b355d7a6ec073ca9707a6133e2477ed.jpg)  
**Text:** "a small dog standing next to a cat"  
**Confidence**: 0.26458819815902784  
**Tags**: "outdoor" "dog" "mammal" "animal" "small" "black" "standing" "brown" "white" "toy" "sitting" "cat" "looking" "bear" "little" "playing" "top" "walking" "stuffed" "eating"

* * *

![](http://cdn.sotong.io/insta/2f8539dad763724a63d7eb4d14d04db3.jpg)  
**Text:** "a can of soda"  
**Confidence**: 0.26328508640396564  
**Tags**: "table" "sitting" "night" "large" "top" "lit" "can" "standing" "light" "red" "old" "cake" "room" "street" "city" "gold" "man" "clock" "white" "phone"

* * *

![](http://cdn.sotong.io/insta/232a248b2db94ca88e089f7b37ae5382.jpg)  
**Text:** "a large building"  
**Confidence**: 0.2619475985323003  
**Tags**: "building" "outdoor" "front" "table" "sitting" "top" "large" "standing" "city" "man" "street" "riding"

* * *

![](http://cdn.sotong.io/insta/bc9c50342affd176b320baebf882b068.jpg)  
**Text:** "a group of people on a bridge"  
**Confidence**: 0.2612594978604784  
**Tags**: "outdoor" "grass" "building" "ship" "group" "people" "harbor" "man" "bunch" "standing" "top" "large" "many" "several" "walking" "street" "hill" "field" "water" "bridge" "herd" "city" "ocean" "traffic" "parked" "riding" "river"

* * *

![](http://cdn.sotong.io/insta/05b432020daeb041741b29f85c8ffe58.jpg)  
**Text:** "a bird sits on a brick wall"  
**Confidence**: 0.26103871152311436  
**Tags**: "building" "outdoor" "sitting" "stone" "top" "brick" "wooden" "green" "large" "old" "bench" "bird" "standing" "eating"

* * *

![](http://cdn.sotong.io/insta/8c8ddb072b0db36192bbd982e963e3da.jpg)  
**Text:** "a red park bench next to a bridge"  
**Confidence**: 0.25938234130599563  
**Tags**: "fence" "outdoor" "red" "building" "bench" "sitting" "park" "train" "bridge" "wooden" "flower" "colored" "colorful" "bushes" "track" "garden" "forest" "large" "white" "field" "man"

* * *

![](http://cdn.sotong.io/insta/4130ec4720d98fa8e78562bcc88c59f5.jpg)  
**Text:** "a close up of a red umbrella"  
**Confidence**: 0.2585984009357427  
**Tags**: "red" "umbrella" "sitting" "large" "blue" "close" "water" "white" "bird" "standing" "room"

* * *

![](http://cdn.sotong.io/insta/1e68a35802875b6eee480ef685c208d1.jpg)  
**Text:** "a fire hydrant next to a window"  
**Confidence**: 0.25791804980874167  
**Tags**: "window" "building" "living" "room" "fire" "water" "snow" "sitting" "area" "old" "door" "table" "river" "covered" "city" "street" "bed" "blue" "hydrant" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/f47e8ad0f3474889832ac29b3734c67c.jpg)  
**Text:** "a plate with a piece of bread"  
**Confidence**: 0.2556445889118278  
**Tags**: "table" "food" "sitting" "plate" "top" "bread" "small" "wooden" "white" "chocolate" "orange" "meat" "laying"

* * *

![](http://cdn.sotong.io/insta/447b145bc6e096ad7e1a689f99fe0703.jpg)  
**Text:** "a boat that is sitting on a table"  
**Confidence**: 0.2553123412068991  
**Tags**: "building" "table" "water" "sitting" "food" "dog" "boat" "hot" "bench" "counter" "top" "large" "man" "red" "people" "city" "parked" "kitchen" "train" "street" "laying" "track" "pizza" "group" "standing" "plate" "white" "riding" "river"

* * *

![](http://cdn.sotong.io/insta/ab81808c039fac760fce4125ac6599dd.jpg)  
**Text:** "a clock sitting in the middle of the room"  
**Confidence**: 0.25468000900230003  
**Tags**: "indoor" "table" "sitting" "room" "chair" "small" "living" "top" "clock" "old" "desk" "brown" "white"

* * *

![](http://cdn.sotong.io/insta/75dba60887b3f5037f5cb62dc855aa95.jpg)  
**Text:** "a statue in front of a building"  
**Confidence**: 0.25332625457060926  
**Tags**: "building" "outdoor" "front" "statue" "black" "bench" "sitting" "large" "roof" "top" "standing" "city" "castle" "man" "park" "clock" "water" "riding" "young" "tower" "street" "boat" "window"

* * *

![](http://cdn.sotong.io/insta/017b2964656c0f7226d9e779abb6dbd3.jpg)  
**Text:** "a group of people sitting at a bar"  
**Confidence**: 0.2508593425503994  
**Tags**: "indoor" "person" "large" "sitting" "table" "building" "filled" "hall" "full" "people" "many" "wooden" "man" "front" "wine" "group" "bunch" "bar" "glasses" "standing" "store" "kitchen" "room"

* * *

![](http://cdn.sotong.io/insta/2f103062244f35a4325048e7edabd474.jpg)  
**Text:** "the tower of the building"  
**Confidence**: 0.24934050121583287  
**Tags**: "outdoor" "building" "large" "old" "top" "front" "church" "sitting" "tall" "clock" "standing" "table" "city" "tower" "man" "train" "street" "walking" "yellow" "pole" "white" "sign" "people" "snow" "riding" "traffic"

* * *

![](http://cdn.sotong.io/insta/1c943572e56a1e17a7940380230ef669.jpg)  
**Text:** "a group of giraffe standing next to a forest"  
**Confidence**: 0.24858975189367902  
**Tags**: "outdoor" "animal" "mammal" "grass" "deer" "food" "standing" "path" "area" "park" "walking" "dirt" "small" "forest" "group" "top" "side" "field" "rocky" "green" "bird" "giraffe" "grazing" "white"

* * *

![](http://cdn.sotong.io/insta/4ccccc09106a3d2d4ed0d173a4af2f8f.jpg)  
**Text:** "a pile of hay"  
**Confidence**: 0.24723975124586525  
**Tags**: "animal" "looking" "hay" "black" "large" "night" "blue" "light" "standing" "white" "man" "field"

* * *

![](http://cdn.sotong.io/insta/d62f72b33f3f38fd7165f0ff3d5bc5d5.jpg)  
**Text:** "a sign in front of a cake"  
**Confidence**: 0.24655355402386825  
**Tags**: "sign" "old" "cake" "sitting"

* * *

![](http://cdn.sotong.io/insta/e6f9e58b58e7ad622a072093af9701bd.jpg)  
**Text:** "a motorcycle parked in front of a fireplace"  
**Confidence**: 0.24150895903935282  
**Tags**: "building" "outdoor" "road" "street" "front" "sitting" "fire" "fireplace" "truck" "parked" "old" "man" "sidewalk" "city" "motorcycle" "standing" "room" "living" "woman" "table" "large" "white" "sign" "people" "riding" "snow"

* * *

![](http://cdn.sotong.io/insta/9a18b521fe1683649f95efa5b59c7929.jpg)  
**Text:** "a group of people walking down a street talking on a cell phone"  
**Confidence**: 0.2413004828036236  
**Tags**: "person" "group" "holding" "people" "standing" "man" "young" "walking" "woman" "playing" "street" "soccer" "city" "talking" "game"

* * *

![](http://cdn.sotong.io/insta/4687a05bdf85d56e8794506fb6aa31a7.jpg)  
**Text:** "a harbor with boats in the ocean"  
**Confidence**: 0.24051896993872088  
**Tags**: "water" "outdoor" "ocean" "beach" "sea" "city" "large" "many" "ship" "view" "harbor" "full" "lot" "body" "top" "mountain" "bunch" "busy" "boat" "umbrella" "group" "people" "flying" "blue"

* * *

![](http://cdn.sotong.io/insta/ae39bee7c0ff819a35e75f971f842e2c.jpg)  
**Text:** "a group of people standing next to a tree"  
**Confidence**: 0.24037874500946452  
**Tags**: "outdoor" "tree" "street" "people" "front" "group" "park" "sitting" "bus" "parked" "water" "man" "standing" "large" "parking" "lot" "walking" "city" "clock" "white" "bench" "riding" "field" "boat" "river"

* * *

![](http://cdn.sotong.io/insta/94dc31a6ac12d9851b3058df608c5dd6.jpg)  
**Text:** "a vase of flowers next to a tree"  
**Confidence**: 0.23991528538277132  
**Tags**: "outdoor" "tree" "sitting" "building" "palm" "front" "flower" "small" "green" "park" "large" "water" "field" "bench" "tall" "vase" "yellow" "tower" "holding" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/44f53627b465f9a76fffe45dd5bdffd9.jpg)  
**Text:** "a doughnut on a city street"  
**Confidence**: 0.23813102134111727  
**Tags**: "outdoor" "building" "water" "doughnut" "large" "donut" "city" "man" "bird" "covered" "snow" "white" "air" "tall" "elephant" "standing"

* * *

![](http://cdn.sotong.io/insta/2ac08338fc86f5ba14a8019bafc5b7a4.jpg)  
**Text:** "a display in a room"  
**Confidence**: 0.23324317612057585  
**Tags**: "indoor" "table" "sitting" "computer" "keyboard" "filled" "desk" "room" "area" "top" "counter" "red" "colorful" "large" "laptop" "covered" "food" "kitchen" "white" "display" "blue"

* * *

![](http://cdn.sotong.io/insta/afa7b4331eee604b26ebbd9b7b3c92a0.jpg)  
**Text:** "a dog sitting in front of a window"  
**Confidence**: 0.23242002146008045  
**Tags**: "indoor" "building" "window" "sitting" "table" "white" "room" "dog" "front" "small" "brown" "large" "counter" "living" "luggage" "laying" "kitchen"

* * *

![](http://cdn.sotong.io/insta/990f6c767ed5e54689a9f26e94fcdc08.jpg)  
**Text:** "a man and woman cutting a cake"  
**Confidence**: 0.23133852434284888  
**Tags**: "person" "building" "table" "cake" "man" "woman" "cutting" "standing" "people" "food" "cut" "military" "group" "uniform" "large" "holding" "store" "white" "blue"

* * *

![](http://cdn.sotong.io/insta/a958510d7fd6f0174cc5f3399ae0eec1.jpg)  
**Text:** "a group of people sitting at a table in front of a building"  
**Confidence**: 0.22982674770802103  
**Tags**: "building" "table" "front" "sitting" "large" "black" "man" "group" "people" "standing" "train" "water" "city" "store" "white" "display" "clock" "street"

* * *

![](http://cdn.sotong.io/insta/0ee7cbe4f1b72afd34c6e5f97c0f59e0.jpg)  
**Text:** "a banana sitting next to a stuffed animal"  
**Confidence**: 0.22119529856545986  
**Tags**: "indoor" "banana" "sitting" "table" "small" "apple" "holding" "yellow" "front" "bowl" "face" "top" "orange" "stuffed" "large" "head" "laying" "white"

* * *

![](http://cdn.sotong.io/insta/7a9f96ae75efdecb3b85e9274e966f18.jpg)  
**Text:** "a stuffed animal toy"  
**Confidence**: 0.21995618734917358  
**Tags**: "grass" "toy" "outdoor" "thing" "sitting" "man" "doll" "large" "park" "top" "horse" "table" "riding" "bear" "white" "holding" "red" "woman" "track" "field" "standing" "train" "parked" "blue" "city" "air" "stuffed" "street"

* * *

![](http://cdn.sotong.io/insta/d60ba99afae655cfb90042de237efef2.jpg)  
**Text:** "a large tall building with a clock tower in the middle of a field"  
**Confidence**: 0.21892471252020124  
**Tags**: "outdoor" "grass" "building" "large" "field" "bridge" "tower" "front" "clock" "view" "green" "standing" "top" "tall" "city" "park" "river" "grazing" "white" "group" "blue"

* * *

![](http://cdn.sotong.io/insta/09a7ba83f6c72ddb75e4dd3cace53370.jpg)  
**Text:** "a statue of a bear behind a tree"  
**Confidence**: 0.2185381677449629  
**Tags**: "outdoor" "plant" "tree" "bear" "standing" "teddy" "sitting" "statue" "large" "forest" "black" "woman" "holding" "park" "man" "purple" "stuffed" "field"

* * *

![](http://cdn.sotong.io/insta/ae72d15e4607883389a930830aa9a390.jpg)  
**Text:** "a group of people on a bridge over water"  
**Confidence**: 0.2182991010269822  
**Tags**: "water" "outdoor" "boat" "ship" "large" "bridge" "man" "people" "harbor" "river" "city" "pier" "riding" "lake" "body" "jet" "group" "standing" "traveling" "cloudy" "dock" "white" "plane" "bird" "air" "ocean"

* * *

![](http://cdn.sotong.io/insta/e435a550c9855f0032a8ff26fc2d8924.jpg)  
**Text:** "a group of people standing outside of a food truck"  
**Confidence**: 0.21733055394438702  
**Tags**: "building" "outdoor" "grass" "table" "standing" "food" "man" "people" "group" "large" "truck" "woman" "white" "parked" "display" "eating" "board" "bus"

* * *

![](http://cdn.sotong.io/insta/42aec3c8fa5a8bba91e7f80d41dd70ea.jpg)  
**Text:** "a bird that is flying in the sky"  
**Confidence**: 0.21514619613090355  
**Tags**: "animal" "lizard" "reptile" "outdoor" "small" "snow" "dog" "white" "brown" "water" "flying" "man" "air" "bird" "large" "standing" "branch"

* * *

![](http://cdn.sotong.io/insta/1dacadae265b97d36a24f6d498bac006.jpg)  
**Text:** "a dog laying on a couch"  
**Confidence**: 0.21218491044743581  
**Tags**: "indoor" "dog" "sitting" "top" "small" "laying" "table" "large" "bed" "standing" "white" "playing"

* * *

![](http://cdn.sotong.io/insta/6c8b2772473363812178936fdf9a62f7.jpg)  
**Text:** "a bus that is sitting in a dark room"  
**Confidence**: 0.20932050447869582  
**Tags**: "indoor" "table" "sitting" "room" "dark" "light" "night" "view" "lit" "red" "large" "black" "mirror" "water" "man" "phone" "bus" "fire"

* * *

![](http://cdn.sotong.io/insta/1c08a552e6c1643bfdcc5cda9c6dab0b.jpg)  
**Text:** "a table with wine glasses"  
**Confidence**: 0.20611447620496262  
**Tags**: "table" "indoor" "sitting" "wooden" "large" "top" "wine" "man" "room" "water" "standing" "white"

* * *

![](http://cdn.sotong.io/insta/3dd0f62e54de65120d7ca0ee07525966.jpg)  
**Text:** "a woman in a restaurant"  
**Confidence**: 0.20595750882635533  
**Tags**: "indoor" "ceiling" "table" "woman" "food" "people" "sitting" "computer" "room" "white" "kitchen" "large" "cake" "eating" "standing" "man" "desk" "display" "restaurant" "group" "playing" "video" "water" "pizza" "sign"

* * *

![](http://cdn.sotong.io/insta/91043a0545d0c9cdf458091afbab4258.jpg)  
**Text:** "a wooden bench sitting next to a guitar"  
**Confidence**: 0.19942693210116233  
**Tags**: "sitting" "wooden" "bench" "guitar" "top" "black" "blue" "park" "laying"

* * *

![](http://cdn.sotong.io/insta/2abb761fdabcf81a909b9b52ae69659f.jpg)  
**Text:** "a group of people sitting on a bench next to a window"  
**Confidence**: 0.19734909610999177  
**Tags**: "table" "people" "chair" "window" "sitting" "group" "mountain" "filled" "front" "woman" "bench" "man" "living" "furniture" "food" "park" "city" "room" "large" "standing" "holding" "umbrella" "water" "doing" "young" "dog" "riding" "air" "playing"

* * *

![](http://cdn.sotong.io/insta/ed91be2723e5b33f996c1a81499f3d20.jpg)  
**Text:** "a pan of food"  
**Confidence**: 0.1958728331938125  
**Tags**: "food" "sitting" "meat" "top" "filled" "red" "fork" "pizza" "pan" "man" "white"

* * *

![](http://cdn.sotong.io/insta/2a357948acda92ee88d3de0a0212daeb.jpg)  
**Text:** "a large building"  
**Confidence**: 0.19541735450726452  
**Tags**: "building" "indoor" "large" "table" "hall" "standing" "man" "room" "people" "hanging" "train" "woman" "luggage" "bridge" "clock" "station" "white"

* * *

![](http://cdn.sotong.io/insta/e679f462d353529a43643d17e2a9c395.jpg)  
**Text:** "a view of a train station next to a bridge"  
**Confidence**: 0.19275564120765398  
**Tags**: "building" "train" "bridge" "outdoor" "water" "large" "view" "overlooking" "sitting" "track" "platform" "long" "subway" "city" "station" "boat" "passenger" "river" "glass" "table" "standing" "parked" "room" "white" "traveling"

* * *

![](http://cdn.sotong.io/insta/502d1b01c207aa51f7515f6fad1eed67.jpg)  
**Text:** "a group of people sitting on a bench"  
**Confidence**: 0.1877279106480098  
**Tags**: "outdoor" "person" "yellow" "sitting" "people" "street" "light" "front" "man" "traffic" "hydrant" "bench" "water" "young" "large" "standing" "walking" "group" "riding" "motorcycle" "woman" "city"

* * *

![](http://cdn.sotong.io/insta/c724e9771bf007d8cc2e58d302a89da8.jpg)  
**Text:** "a vase of flowers sitting on a bench in front of a building"  
**Confidence**: 0.18687048619992677  
**Tags**: "outdoor" "building" "table" "house" "sitting" "front" "yellow" "fire" "bench" "sidewalk" "street" "hydrant" "tree" "walking" "giraffe" "man" "large" "garden" "bushes" "wooden" "umbrella" "white" "standing" "palm" "red" "laying" "vase" "dirt"

* * *

![](http://cdn.sotong.io/insta/a5bc4bb86885338d1a70a7957391df7d.jpg)  
**Text:** "a vase of flowers on a window sill"  
**Confidence**: 0.1857560946746947  
**Tags**: "building" "window" "door" "sign" "front" "sitting" "red" "table" "painted" "view" "room" "standing" "stop" "hanging" "white" "wooden" "covered" "large" "glass" "graffiti" "sun" "pole" "living" "kitchen" "vase"

* * *

![](http://cdn.sotong.io/insta/d3f38287c10c0ce345af7772e6d6b93e.jpg)  
**Text:** "the tower of the building"  
**Confidence**: 0.18348472085473144  
**Tags**: "outdoor" "building" "large" "tower" "clock" "top" "old" "church" "sitting" "stone" "cloudy" "white" "sheep" "snow" "standing" "brick" "field" "tall" "blue"

* * *

![](http://cdn.sotong.io/insta/d84556e2fe66586f0a3188f6d2e6dfa1.jpg)  
**Text:** "a large mirror"  
**Confidence**: 0.17650171813314328  
**Tags**: "indoor" "table" "sitting" "large" "top" "room" "black" "white" "brick" "mirror" "kitchen"

* * *

![](http://cdn.sotong.io/insta/63a9c9a529b765479b58f940821c420b.jpg)  
**Text:** "a church with a large building"  
**Confidence**: 0.17613439935866163  
**Tags**: "outdoor" "building" "large" "church" "front" "sitting" "top" "standing" "old" "white" "walking" "clock" "blue" "cloudy" "tower" "tall" "people" "city" "parked" "snow" "group"

* * *

![](http://cdn.sotong.io/insta/a518966caa53b483eb84c2181416d71e.jpg)  
**Text:** "a group of pink umbrellas"  
**Confidence**: 0.17594362567481667  
**Tags**: "pink" "red" "table" "colored" "top" "large" "covered" "different" "standing" "display" "umbrella" "woman" "playing" "group" "animal" "bear"

* * *

![](http://cdn.sotong.io/insta/7e4bb57eb1f944690ffee3c3973b5497.jpg)  
**Text:** "a bunch of food on a grill"  
**Confidence**: 0.1753024662971872  
**Tags**: "food" "wire" "filled" "sitting" "table" "bunch" "covered" "group" "top" "grill" "blue" "shrimp"

* * *

![](http://cdn.sotong.io/insta/a7e9d61968fdfe6f7dacfc913b025f50.jpg)  
**Text:** "a person sitting on a table"  
**Confidence**: 0.17450400660467555  
**Tags**: "indoor" "sitting" "table" "top" "phone" "white" "cat"

* * *

![](http://cdn.sotong.io/insta/287c3a3912ed6d5e93971ece995c6b1d.jpg)  
**Text:** "a table topped with different types of food on a stove"  
**Confidence**: 0.17406512026369775  
**Tags**: "indoor" "table" "food" "small" "sitting" "counter" "items" "top" "kitchen" "plate" "filled" "man" "different" "white" "cake" "sink" "woman" "holding" "oven" "standing" "stove"

* * *

![](http://cdn.sotong.io/insta/c87e9d0a84bf6f6846f6770b85994ac3.jpg)  
**Text:** "a clock tower in front of a building"  
**Confidence**: 0.17345088555819527  
**Tags**: "outdoor" "building" "large" "top" "front" "tower" "sitting" "clock" "stone" "white" "standing" "city" "tall" "old" "walking" "brick" "water" "field" "street" "parked" "people" "group"

* * *

![](http://cdn.sotong.io/insta/c1ab90d96128ea5d02c461795dfad8b6.jpg)  
**Text:** "a pan of food on a plate"  
**Confidence**: 0.17141502585773793  
**Tags**: "animal" "plate" "table" "sitting" "food" "metal" "bowl" "pan" "top" "cake" "filled" "meat" "fork" "sauce" "black" "large" "covered" "cheese" "knife" "hot" "pizza" "stove" "white"

* * *

![](http://cdn.sotong.io/insta/b35f6769d4ba96bc08253077aceb0ec5.jpg)  
**Text:** "a close up of food on a table"  
**Confidence**: 0.16958688907573582  
**Tags**: "table" "food" "sitting" "eating" "black" "water" "glass" "laying" "holding" "plate" "pizza"

* * *

![](http://cdn.sotong.io/insta/506f0846f1fe1fe3ca059b6d7c01b807.jpg)  
**Text:** "a traffic light next to a tree"  
**Confidence**: 0.16701346412319037  
**Tags**: "outdoor" "light" "traffic" "group" "street" "tree" "hill" "large" "field" "standing" "sunset" "people" "sun" "air" "man" "city" "snow" "water" "game" "skiing" "slope" "sky"

* * *

![](http://cdn.sotong.io/insta/eb099faa036ef1554b86ceb5cbda85fb.jpg)  
**Text:** "a room with a couch a table and chairs"  
**Confidence**: 0.16693453556500404  
**Tags**: "indoor" "table" "chair" "sitting" "room" "area" "green" "large" "kitchen" "hanging" "living" "standing" "wooden" "white" "group" "people"

* * *

![](http://cdn.sotong.io/insta/983589d19b3b575ed7bc8744b991f03a.jpg)  
**Text:** "a group of people flying kites in a pool of water"  
**Confidence**: 0.1664502783641798  
**Tags**: "water" "outdoor" "lake" "large" "flying" "sitting" "top" "body" "boat" "people" "swimming" "kite" "bird" "man" "pool" "riding" "group" "air" "dock" "floating" "park" "river" "standing" "surfing" "city" "ocean"

* * *

![](http://cdn.sotong.io/insta/af0b8d0a1a753619f2da5f875e2e7935.jpg)  
**Text:** "a bird sitting on top of a tree"  
**Confidence**: 0.16590487691876754  
**Tags**: "outdoor" "tree" "front" "building" "sitting" "standing" "wooden" "bench" "man" "brown" "garden" "red" "large" "park" "group" "palm" "table" "bird" "holding" "tall" "water" "white" "zoo" "riding" "phone" "people"

* * *

![](http://cdn.sotong.io/insta/3562bb1712ac50a6b10c320b41ca3af5.jpg)  
**Text:** "a group of people with wine glasses"  
**Confidence**: 0.1640203961305865  
**Tags**: "person" "indoor" "building" "hall" "large" "table" "people" "auditorium" "wine" "sitting" "many" "filled" "group" "wooden" "full" "glasses" "bunch" "man" "standing" "kitchen" "red" "crowd" "room"

* * *

![](http://cdn.sotong.io/insta/d8be0c3dcf7e53e5ffa8f05a08888ac8.jpg)  
**Text:** "a tray of hot dogs on a grill"  
**Confidence**: 0.16257163201106437  
**Tags**: "animal" "food" "hot" "grill" "tray" "table" "top" "dog" "sitting" "filled" "meat" "knife" "plate" "cooking" "cooked" "large" "sandwich" "fries" "covered" "bun" "pan" "cake" "cheese" "hotdog" "man"

* * *

![](http://cdn.sotong.io/insta/ebb1e03a79398c289b62c7378be799d7.jpg)  
**Text:** "a crowd of people standing on top of a building"  
**Confidence**: 0.16233855657954568  
**Tags**: "building" "people" "large" "many" "group" "table" "train" "walking" "crowd" "standing" "yellow" "clock" "riding" "luggage"

* * *

![](http://cdn.sotong.io/insta/203ad8ba4a397ad95e00e9bdcc2b3e6e.jpg)  
**Text:** "a large clock tower towering over a city"  
**Confidence**: 0.15538618100191784  
**Tags**: "outdoor" "building" "large" "background" "top" "clock" "tower" "big" "city" "front" "skyscraper" "sitting" "tall" "yellow" "white" "street" "blue" "flying" "standing"

* * *

![](http://cdn.sotong.io/insta/2d5c8c0ac30a1d6b6cd7b01b02c03d37.jpg)  
**Text:** "a bed with a mountain in the window"  
**Confidence**: 0.15529551086907875  
**Tags**: "mountain" "window" "table" "overlooking" "view" "water" "sitting" "building" "top" "city" "bed" "glass" "ocean" "large" "room" "phone" "river" "white"

* * *

![](http://cdn.sotong.io/insta/218db713e08bea7b8c62cc51aba96064.jpg)  
**Text:** "a large cake"  
**Confidence**: 0.15284657901927493  
**Tags**: "outdoor" "covered" "large" "side" "sitting" "food" "table" "top" "street" "old" "cake" "beach" "ocean" "snow" "bird" "laying"

* * *

![](http://cdn.sotong.io/insta/df340e0130f2876014f3eb8c65f492ef.jpg)  
**Text:** "a bird that is standing in the rain"  
**Confidence**: 0.15240179546915875  
**Tags**: "nature" "rain" "water" "large" "covered" "table" "group" "bird" "red" "field" "white" "standing"

* * *

![](http://cdn.sotong.io/insta/a0bbe853ef4b73897a96bdcc9e635eb2.jpg)  
**Text:** "person sitting on a table next to a window"  
**Confidence**: 0.1495132572460848  
**Tags**: "screen" "building" "indoor" "table" "window" "sitting" "woman" "top" "room" "man" "kitchen" "standing" "white" "people"

* * *

![](http://cdn.sotong.io/insta/91e8298f09d88282244a424b1abdc5e3.jpg)  
**Text:** "a man holding a frisbee"  
**Confidence**: 0.1466220814468727  
**Tags**: "person" "outdoor" "man" "road" "holding" "street" "front" "standing" "hand" "board" "young" "walking" "riding" "playing" "water" "parking" "frisbee" "city" "white"

* * *

![](http://cdn.sotong.io/insta/61ee94a932887ec3e91339524c39090b.jpg)  
**Text:** "a group of people standing outside of a building"  
**Confidence**: 0.1463443377161196  
**Tags**: "outdoor" "building" "standing" "people" "man" "top" "boat" "large" "sitting" "table" "group" "orange" "board" "row" "yellow" "holding" "woman" "water" "hot" "riding"

* * *

![](http://cdn.sotong.io/insta/c037f999ac5e0d0c5965c0142fa5cbe6.jpg)  
**Text:** "a bus that is parked next to a tree"  
**Confidence**: 0.14056013503830111  
**Tags**: "outdoor" "bus" "street" "parked" "tree" "lined" "group" "driving" "double" "large" "park" "people" "city" "traveling" "decker" "water" "several" "lot" "white" "parking" "standing" "riding" "river" "man" "clock" "station" "boat" "track" "train" "field"

* * *

![](http://cdn.sotong.io/insta/406e8877b5ad66625fec6862e0b3e6c6.jpg)  
**Text:** "a tower with a clock on the side of a building"  
**Confidence**: 0.13994269355926145  
**Tags**: "building" "outdoor" "clock" "red" "large" "tower" "top" "city" "sitting" "tall" "blue" "side" "brick" "view" "train" "white" "flying" "street" "sign"

* * *

![](http://cdn.sotong.io/insta/46d6fc71ee505540cd2057d422856132.jpg)  
**Text:** "a group of people standing on top of a building"  
**Confidence**: 0.1299945030067127  
**Tags**: "person" "building" "photo" "people" "woman" "table" "group" "different" "man" "standing" "large" "display" "walking" "umbrella" "hanging" "room" "sign" "doing" "holding" "food" "street" "playing" "white" "riding" "city"

* * *

![](http://cdn.sotong.io/insta/2fe5d706e374d96dbbb45ba01e3381d5.jpg)  
**Text:** "a man sitting in front of a building"  
**Confidence**: 0.12787021858265818  
**Tags**: "outdoor" "green" "man" "sitting" "old" "looking" "building" "top" "face" "large" "standing" "yellow" "white" "field"

* * *

![](http://cdn.sotong.io/insta/ac765dcd38de73290e0a62252a819c9b.jpg)  
**Text:** "a clock tower in the air"  
**Confidence**: 0.12682173461543872  
**Tags**: "outdoor" "building" "tower" "air" "skyscraper" "high" "cloudy" "green" "day" "blue" "clock" "top" "large" "plane" "trick" "old" "tall" "flying" "riding" "doing" "ramp" "man" "snow" "white"

* * *

![](http://cdn.sotong.io/insta/9d68bc4104b4e56867b1dd98b213b2fe.jpg)  
**Text:** "a bridge over water"  
**Confidence**: 0.11649621646263085  
**Tags**: "building" "water" "table" "sitting" "top" "boat" "man" "large" "old" "river" "city" "board" "bridge" "food" "white" "train" "riding" "street" "standing" "room" "track" "pizza" "kitchen" "people"

* * *

![](http://cdn.sotong.io/insta/a08627ef4739a7da9fba015df1549702.jpg)  
**Text:** "a boat that is sitting on a window sill"  
**Confidence**: 0.1137135753224548  
**Tags**: "mountain" "building" "window" "water" "large" "view" "sitting" "table" "top" "boat" "man" "green" "old" "people" "train" "white" "board" "standing" "ocean" "double" "city"

* * *

![](http://cdn.sotong.io/insta/04f1cb6899838905cf895c37d134683d.jpg)  
**Text:** "a man standing next to a fire hydrant"  
**Confidence**: 0.11125878223814174  
**Tags**: "outdoor" "building" "man" "street" "water" "red" "standing" "old" "woman" "walking" "holding" "wearing" "young" "hydrant" "people" "city" "fire" "phone" "cat" "bear" "stuffed"

* * *

![](http://cdn.sotong.io/insta/fa533c7525135d8fb10a17adaeb405fc.jpg)  
**Text:** "a bunch of items that are sitting in a shop"  
**Confidence**: 0.1108200539065315  
**Tags**: "building" "outdoor" "photo" "covered" "street" "items" "sitting" "various" "decorated" "many" "store" "area" "man" "different" "colorful" "shop" "table" "graffiti" "bunch" "living" "old" "walking" "young" "dog" "luggage" "room" "city" "woman" "standing" "suitcase" "fire" "board" "group" "sign"

* * *

![](http://cdn.sotong.io/insta/d274458e563a3e547cfa99070d74d607.jpg)  
**Text:** "a large sign"  
**Confidence**: 0.10955033303752869  
**Tags**: "text" "large" "man" "sign" "standing"

* * *

![](http://cdn.sotong.io/insta/9b60e42e0f86fee89c24dfe78680768e.jpg)  
**Text:** "a picture of some sort"  
**Confidence**: 0.10506834378853601  
**Tags**: "text"

* * *

![](http://cdn.sotong.io/insta/24c8166575b930d25a0df955f85d5135.jpg)  
**Text:** "an umbrella sitting on top of a building"  
**Confidence**: 0.10023965372593548  
**Tags**: "building" "table" "sitting" "front" "truck" "decorated" "hanging" "store" "wooden" "street" "large" "umbrella" "man" "sign" "standing" "night"

* * *

![](http://cdn.sotong.io/insta/77e4299db2252a3c218ddf4f4d4bf06d.jpg)  
**Text:** "a table topped with lots of windows"  
**Confidence**: 0.09547554589433928  
**Tags**: "indoor" "table" "building" "sitting" "many" "filled" "old" "large" "room" "covered" "fire" "people" "man" "group"

* * *

![](http://cdn.sotong.io/insta/8c19f3caa3e07e9102380ee450c98f62.jpg)  
**Text:** "a number of stuffed animals sitting next to a building"  
**Confidence**: 0.08841432049250653  
**Tags**: "outdoor" "building" "sitting" "top" "large" "bear" "stuffed" "table" "old" "food" "white" "man" "riding" "street"

* * *

![](http://cdn.sotong.io/insta/73011751645ccde255588ee466f1e5bc.jpg)  
**Text:** "a group of people on a bridge"  
**Confidence**: 0.08731609403534804  
**Tags**: "building" "outdoor" "view" "water" "mountain" "front" "overlooking" "man" "large" "standing" "orange" "people" "city" "river" "bench" "bridge" "group" "riding" "ocean" "horse" "plane" "train"

* * *

![](http://cdn.sotong.io/insta/7e5c59843aafd1f12dbd007d92123589.jpg)  
**Text:** "a red bench"  
**Confidence**: 0.08554099750278843  
**Tags**: "outdoor" "building" "sitting" "red" "small" "black" "bench" "standing" "large" "man" "holding" "street" "city"

* * *

![](http://cdn.sotong.io/insta/1cad17f3fa91689d5d596afe5c33d571.jpg)  
**Text:** "a close up of food on a fish in the snow"  
**Confidence**: 0.08144534940545779  
**Tags**: "animal" "snow" "food" "fish" "dog" "covered" "sitting" "plate" "large" "top" "knife" "laying" "table" "white" "cake" "man" "red"

* * *

![](http://cdn.sotong.io/insta/e68f6d24e965f195f9a0c6acd94b721c.jpg)  
**Text:** "a red train parked in front of a building"  
**Confidence**: 0.07984377671688402  
**Tags**: "building" "indoor" "train" "red" "sitting" "table" "large" "room" "rug" "platform" "station" "white" "parked"

* * *

![](http://cdn.sotong.io/insta/dc6ee6816a004a4fb5be29c3a0cea116.jpg)  
**Text:** "a clock sitting in front of a window"  
**Confidence**: 0.07894240869517427  
**Tags**: "building" "indoor" "clock" "large" "window" "sitting" "glass" "light" "room" "table" "lit" "many" "standing" "group" "city" "church" "night" "tall"

* * *

![](http://cdn.sotong.io/insta/cce7fcf30985340f2685fcd170481859.jpg)  
**Text:** "a bunch of items that are on a shelf"  
**Confidence**: 0.077719202284831  
**Tags**: "photo" "items" "many" "bunch" "different" "various" "computer" "table" "old" "covered" "food" "board" "machine" "man" "laying" "refrigerator"

* * *

![](http://cdn.sotong.io/insta/e64b75c2eddfec3c6e53c43c4b546ccf.jpg)  
**Text:** "a group of men riding on the back of a cage"  
**Confidence**: 0.07364281229166424  
**Tags**: "building" "covered" "decorated" "man" "large" "table" "snow" "cage" "group" "white" "riding" "fire" "board" "street" "standing" "sign" "people"

* * *

![](http://cdn.sotong.io/insta/8c0ea296177c7b547abfba7bdb17f8ea.jpg)  
**Text:** "a red and white sign"  
**Confidence**: 0.07146685737358643  
**Tags**: "sitting" "room" "black" "side" "white" "train" "bus" "sign" "red" "city" "parked" "man" "street"

* * *

![](http://cdn.sotong.io/insta/73b019419c607d60d2172fdb99f5d34e.jpg)  
**Text:** "a street scene with focus on a rainy day"  
**Confidence**: 0.07119725579722257  
**Tags**: "building" "outdoor" "street" "city" "rain" "snow" "walking" "man" "covered" "holding" "standing" "train" "group" "riding" "umbrella" "track" "woman" "rainy" "water" "people" "white" "boat" "sign" "bus" "hydrant"

* * *

![](http://cdn.sotong.io/insta/c4cceed183b3ab595710478218f599ea.jpg)  
**Text:** "a train that is on top of a car"  
**Confidence**: 0.07080899533332351  
**Tags**: "indoor" "filled" "sitting" "car" "open" "full" "train" "table" "bus" "airplane" "man" "refrigerator" "standing" "road"

* * *

![](http://cdn.sotong.io/insta/22e5ede66c325f703e14aae221db0083.jpg)  
**Text:** "a picture of a building"  
**Confidence**: 0.07067362303626663  
**Tags**: "building"

* * *

![](http://cdn.sotong.io/insta/6196d70de9cb32c051a906bd8081b883.jpg)  
**Text:** "a vase of flowers on a table"  
**Confidence**: 0.07023484236756  
**Tags**: "table" "building" "sitting" "top" "food" "filled" "flower" "woman" "counter" "wooden" "vase" "glass" "man" "fruit" "standing" "room" "plate" "bench" "water" "white" "laying" "dog" "kitchen" "people"

* * *

![](http://cdn.sotong.io/insta/a38cb87b71c19c4ce721e66a50f8309b.jpg)  
**Text:** "a display case"  
**Confidence**: 0.06909110031216706  
**Tags**: "indoor" "table" "sitting" "standing" "red" "room" "black" "woman" "man" "large" "display" "kitchen"

* * *

![](http://cdn.sotong.io/insta/3d59db65d0a1f4bda36a521cac106a9b.jpg)  
**Text:** "in this picture"  
**Confidence**: 0.05922747976692775  
**Tags**:

* * *

![](http://cdn.sotong.io/insta/281a2345f551e8563ee42bbfc62e8cca.jpg)  
**Text:** "a crowd of people"  
**Confidence**: 0.05223630992607654  
**Tags**: "text"

* * *

![](http://cdn.sotong.io/insta/27181186d5b5cb7205f20ca59e53aed4.jpg)  
**Text:** "a close up of an umbrella"  
**Confidence**: 0.04703611562688386  
**Tags**: "text" "outdoor" "water" "field" "umbrella" "large" "standing" "group"

* * *

![](http://cdn.sotong.io/insta/beb66c8fc5136c661ddfa0e66593a06f.jpg)  
**Text:** "a person laying on the floor"  
**Confidence**: 0.04142264158194378  
**Tags**: "indoor" "black" "sitting" "top" "laying" "large"

* * *

![](http://cdn.sotong.io/insta/c2957fd039f7397a387ce25edc4946de.jpg)  
**Text:** "person sitting on top of a building"  
**Confidence**: 0.039917627066425695  
**Tags**: "building" "indoor" "table" "window" "sitting" "man" "room" "woman" "living" "standing" "people" "board" "kitchen" "white" "sink"

* * *

![](http://cdn.sotong.io/insta/de1196010f3e7914044ad8baacc7ba66.jpg)  
**Text:** "two men in suits and ties"  
**Confidence**: 0.030471157874181008  
**Tags**:

* * *

![](http://cdn.sotong.io/insta/e34cd071f96dd111fd89f46c8202a386.jpg)  
**Text:** "a yellow stuffed animal"  
**Confidence**: 0.03001491559310438  
**Tags**: "indoor" "table" "items" "sitting" "photo" "colorful" "fire" "different" "room" "yellow" "	stuffed" "living" "counter" "bear" "woman" "hanging" "walking" "man" "many" "covered" "bedroom" "dog" "store" "white" "large" "standing" "street" "display" "bird" "laying" "bed" "blue" "phone" "kitchen"

* * *

![](http://cdn.sotong.io/insta/606b2728871fcea31bb499ded8a1e841.jpg)  
**Text:** "a couple of giraffes that are next to a map"  
**Confidence**: 0.01453261054260793  
**Tags**: "map"

* * *

![](http://cdn.sotong.io/insta/3ced472425446898f9b8728b741fa746.jpg)  
**Text:** "a couple of giraffes that are next to a map"  
**Confidence**: 0.01153727086975813  
**Tags**: "text" "map"

* * *
