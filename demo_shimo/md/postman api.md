# pm:Object
The pm object encloses all information pertaining to the script being executed and allows one to access a copy of the request being sent or the response received. It also allows one to get and set environment and global variables.

>pm对象包含与正在执行的脚本相关的所有信息。pm对象包含与正在执行的脚本相关的所有信息，并允许用户访问正在发送的请求或接收的响应的副本。它还允许获取和设置环境和全局变量。

---
## pm.info:Object
---------------------------

pm.info.eventName:String --------------test或pre-request

pm.info.iteration:Number --------------第几个

pm.info.iterationCount:Number-------------一共几个

pm.info.requestName:String------------request名称

pm.info.requestId:String ---------------requestId

---------------------------

pm.info 如何获取request名称 => pm.info.requestName:String

pm.info 如何获取iteration 序号 => pm.info.iteration:Number

pm.info 如何获取iteration总数 => pm.info.iterationCount

---------------------------

## pm.info:Object
The pm.info object contains information pertaining to the script being executed. Useful information such as the request name, request Id, and iteration count are stored inside of this object.

>info对象包含与正在执行的脚本相关的信息。诸如请求名、请求Id和迭代计数等有用信息存储在此对象中。

pm.info.eventName:String

* Contains information whether the script being executed is a "prerequest" or a "test" script.
>包含正在执行的脚本是“prerequest”脚本还是“test”脚本的信息。包含正在执行的脚本是“prerequest”脚本还是“test”脚本的信息。

pm.info.iteration:Number

* Is the value of the current iteration being run.
>是当前正在运行的迭代的值。

pm.info.iterationCount:Number

* Is the total number of iterations that are scheduled to run.
>计划运行的迭代总数。

pm.info.requestName:String

* The saved name of the individual request being run.
>计划运行的迭代总数。正在运行的单个请求的保存名称。

pm.info.requestId:String

* The unique guid that identifies the request being run.
>标识正在运行的请求的唯一guid。

---
### 
### pm.sendRequest
**pm.sendRequest:Function**

The pm.sendRequest function allows sending HTTP/HTTPS requests asynchronously. Simply put, with asynchronous scripts, you can execute logic in the background if you have a heavy computational task or are sending multiple requests. Instead of waiting for a call to complete and blocking any next requests, you can designate a callback function and be notified when an underlying operation has finished. 

>sendRequest函数允许异步发送HTTP/HTTPS请求。简单地说，使用异步脚本，如果您有繁重的计算任务或正在发送多个请求，则可以在后台执行逻辑。您可以指定回调函数，并在底层操作完成时收到通知，而不是等待调用完成并阻止任何下一个请求。

Some things to know about pm.sendRequest():

* The method accepts a collection SDK compliant request and a callback. The callback receives two arguments, an error (if any) and an SDK-compliant response. Refer to [Collection SDK Documentation](http://www.postmanlabs.com/postman-collection/Request.html#~definition) to view more information.
* It can be used in the pre-request or the test script.
>关于pm.sendRequest（），需要知道的一些事情：
>该方法接受与集合SDK兼容的请求和回调。回调接收两个参数，一个错误（如果有）和一个符合SDK的响应。请参阅集合SDK文档以查看更多信息。
>它可以在预请求或测试脚本中使用。
```
// example with a plain string URL
pm.sendRequest('https://postman-echo.com/get', function (err, res) {
    if (err) {
        console.log(err);
    } else {
        pm.environment.set("variable_key", "new_value");
    }
});
// Example with a full fledged SDK Request
const echoPostRequest = {
  url: 'https://postman-echo.com/post',
  method: 'POST',
  header: 'headername1:value1',
  body: {
    mode: 'raw',
    raw: JSON.stringify({ key: 'this is json' })
  }
};
pm.sendRequest(echoPostRequest, function (err, res) {
  console.log(err ? err : res.json());
});
// example containing a test ** under the Tests tab only
pm.sendRequest('https://postman-echo.com/get', function (err, res) {
  if (err) { console.log(err); }
  pm.test('response should be okay to process', function () {
    pm.expect(err).to.equal(null);
    pm.expect(res).to.have.property('code', 200);
    pm.expect(res).to.have.property('status', 'OK');
  });
});
```
Extended Reference:
* [Request JSON](http://www.postmanlabs.com/postman-collection/Request.html#~definition)
* [Response Structure](http://www.postmanlabs.com/postman-collection/Response.html)

---

---
### pm.variables
------------------------

pm.variables.has(variableName:String):function → Boolean

pm.variables.get(variableName:String):function → *

pm.variables.set(variableName:String, variableValue:String"):function

pm.variables.replaceIn(variableName:String):function

pm.variables.toObject():function → Object

pm.environment.name:String

pm.environment.has(variableName:String):function → Boolean

pm.environment.get(variableName:String):function → *

pm.environment.set(variableName:String, variableValue:String):function

pm.environment.replaceIn(variableName:String):function

pm.environment.toObject():function → Object

pm.environment.unset(variableName:String):function

pm.environment.clear():function

pm.collectionVariables.has(variableName:String):function → Boolean

pm.collectionVariables.get(variableName:String):function → *

pm.collectionVariables.set(variableName:String, variableValue:String):function

pm.collectionVariables.replaceIn(variableName:String):function

pm.collectionVariables.toObject():function → Object

pm.collectionVariables.unset(variableName:String):function

pm.collectionVariables.clear():function

pm.globals.has(variableName:String):function → Boolean

pm.globals.get(variableName:String):function → *

pm.globals.set(variableName:String, variableValue:String):function

pm.globals.replaceIn(variableName:String):function

pm.globals.toObject():function → Object

pm.globals.unset(variableName:String):function

pm.globals.clear():function

------------------------

本地变量的前3个字母=>vari

本地变量的后续=>iable

本地变量后是否有s=>是

环境变量的前3个字母=>env

环境变量的中间4个字母=>iron

环境变量的后4个字母=>ment

环境变量是否加s=>否

集合变量使用的前缀是什么=>collection

集合变量的后缀是什么=>本地变量名(Variables)

全局变量后是否要加s=>是

全局变量前缀是什么=>glo

全局变量后缀是什么=>bal

变量的基础方法=>get(k),set(k, v),toObject()

变量是否有某个k的方法 =>has(k)

环境变量的独特属性=>name

环境、全局、集合的特有方法=>unset(k),clear()

------------------------

### pm.variables
pm.variables: [Variable SDK Reference](https://www.postmanlabs.com/postman-collection/Variable.html)

In Postman, all variables conform to a specific hierarchy. All variables defined in the current iteration take precedence over the variables defined in the current environment, which overrides ones defined in the global scope. The order of precedence is Iteration Data < Environment < Collection< Global.

* pm.variables.has(variableName:String):function → Boolean: Check if there is a local variable in the current scope.
>检查当前作用域中是否存在局部变量。
* pm.variables.get(variableName:String):function → *: Get the value of the local variable with the specified name.
>获取具有指定名称的局部变量的值。
* pm.variables.set(variableName:String, variableValue:String"):function → void: Set a local variable with the given value.
>使用给定值设置局部变量。
* pm.variables.replaceIn(variableName:String):function: Replaces the dynamic variable {{variable_name}}syntax with its actual resolved value.
>将动态变量{{variable}语法替换为其实际解析值。
* pm.variables.toObject():function → Object: Returns an object containing all the variables in the local scope.
>返回一个包含本地作用域中所有变量的对象。

The variables defined in the individual scopes may also be accessed via pm.environment for the environment scope and pm.globals for the global scope.

>在各个作用域中定义的变量也可以通过pm.environment（环境作用域）和pm.globals（全局作用域）访问。
### ### pm.environment
pm.environment:

* pm.environment.name:String: Contains the name of the current environment.
>包含当前环境的名称。
* pm.environment.has(variableName:String):function → Boolean: Check if the environment has a variable with the given name.
* pm.environment.get(variableName:String):function → *: Get the environment variable with the given name.
* pm.environment.set(variableName:String, variableValue:String):function: Sets an environment variable with the given name and value.
* pm.environment.replaceIn(variableName:String):function: Replaces the dynamic variable {{variable_name}}syntax with its actual resolved value.
* pm.environment.toObject():function → Object: Returns all the environment variables in the form of a single object.
* pm.environment.unset(variableName:String):function: Remove an environment variable with the specified name.
* pm.environment.clear():function: Clears all the current environment variables.
### ### pm.collectionVariables
pm.collectionVariables:

* pm.collectionVariables.has(variableName:String):function → Boolean: Check if there is a collection variable with the given name.
>检查是否存在具有给定名称的集合变量。
* pm.collectionVariables.get(variableName:String):function → *: Returns the value of the collection variable with the given name.
* pm.collectionVariables.set(variableName:String, variableValue:String):function: Sets a collection variable with given value.
* pm.collectionVariables.replaceIn(variableName:String):function: Replaces the dynamic variable {{variable_name}} syntax with its actual resolved value.
* pm.collectionVariables.toObject():function → Object: Returns a list of variables and their values in the form of an object.
* pm.collectionVariables.unset(variableName:String):function: Clears the specified collection variable.
* pm.collectionVariables.clear():function: Clear all the collection variables.
### ### pm.globals
pm.globals:

* pm.globals.has(variableName:String):function → Boolean: Check if there is a global variable with the given name.
>检查是否存在具有给定名称的全局变量。
* pm.globals.get(variableName:String):function → *: Returns the value of the global variable with the given name.
* pm.globals.set(variableName:String, variableValue:String):function: Sets a global variable with given value.
* pm.globals.replaceIn(variableName:String):function: Replaces the dynamic variable {{variable_name}} syntax with its actual resolved value.
* pm.globals.toObject():function → Object: Returns a list of variables and their values in the form of an object.
>以对象的形式返回变量及其值的列表。
* pm.globals.unset(variableName:String):function: Clears the specified global variable.
* 清除指定的全局变量。
* pm.globals.clear():function: Clear all the global variables.
>清除所有全局变量。

---

---
### pm.request
--------------------

pm.request.url:[Url](http://www.postmanlabs.com/postman-collection/Url.html)

pm.request.headers:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html)

pm.request.method:String

pm.request.body:[RequestBody](http://www.postmanlabs.com/postman-collection/RequestBody.html)

pm.request.headers.add(headerName:String):function

pm.request.headers.remove(headerName:String):function

pm.request.headers.upsert({ key: headerName:String, value: headerValue:String}):function)

--------------------

如何看request的url => pm.request.url

如何看request的头是否要加s => 是

如何看request的body => pm.request.body

如何增加headers=>pm.headers.add(标名)

如何删除headers=>pm.headers.remove(标名)

如何更新爱pm.headers后用的是什么=>upsert

--------------------

### pm.request
pm.request: [Request SDK Reference](https://www.postmanlabs.com/postman-collection/Request.html)

The request object inside pm is a representation of the request for which this script is being run. For a pre-request script, this is the request that is about to be sent and when in a test script, this is the representation of the request that was sent.

request contains information stored in the following structure:

>的请求对象是运行此脚本的请求的表示。对于预请求脚本，这是即将发送的请求，在测试脚本中，这是已发送请求的表示。
>请求包含存储在以下结构中的信息：
* pm.request.url:[Url](http://www.postmanlabs.com/postman-collection/Url.html): Contains the URL to which the request is made.
>包含发出请求的URL。
* pm.request.headers:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html): Contains the list of headers for the current request.
* pm.request.method:String The HTTP method of the sent request.
* pm.request.body:[RequestBody](http://www.postmanlabs.com/postman-collection/RequestBody.html): Contains all the data related to the request body.
>包含与请求正文相关的所有数据。
* pm.request.headers.add(headerName:String):function: Adds a header with the specified name for the current request.
* pm.request.headers.remove(headerName:String):function: Deletes the header with the specified name for the current request.
>删除当前请求的具有指定名称的头。
* pm.request.headers.upsert({ key: headerName:String, value: headerValue:String}):function): Inserts a header name and header value as given to the list of headers for the current request (if the header does not exist, otherwise the already existing header is updated to the new value).
>插入给定给当前请求的头列表的头名称和头值（如果头不存在，则已存在的头将更新为新值）。
>**The following items are ONLY available in the test scripts.**

---

---
### pm.response
-------------------

pm.response.code:Number

pm.response.status:String

pm.response.headers:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html)

pm.response.responseTime:Number

pm.response.responseSize:Number

pm.response.text():Function → String

pm.response.json():Function → Object

-------------------

response上有哪几个属性 => 返回码,返回状态，响应时间，返回数据大小

response返回码代码=>code

response返回状态代码=>status

response返回时间代码是什么responseTime

response返回大小代码是什么=>responseSize:number

response方法有哪2个=>返回文本，返回json

response返回数据文本的代码=>text()

response返回数据json是属性还是方法=>方法

response返回数据json的代码=>json()

-------------------

### pm.response
pm.response: [Response SDK Reference](https://www.postmanlabs.com/postman-collection/Response.html)

Inside the test scripts, the pm.response object contains all information pertaining to the response that was received.

>在测试脚本中，pm.response对象包含与接收到的响应相关的所有信息。

The response details are stored in the following format:

* pm.response.code:Number
* pm.response.status:String
* pm.response.headers:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html)
* pm.response.responseTime:Number
* pm.response.responseSize:Number
* pm.response.text():Function → String
* pm.response.json():Function → Object

---

---
### pm.iterationData
------------------------

pm.iterationData.get(variableName:String):function

pm.iterationData.toObject():function → Object:

pm.iterationData.addLayer(list: VariableList):function 

pm.iterationData.clear():function 

pm.iterationData.set(key: string, value: any, type: string):function 

pm.iterationData.syncVariablesFrom(object: {[key: string]: VariableDefinition}, track?: boolean, prune?: boolean):function

>从具有指定名称的对象中获取变量。

pm.iterationData.syncVariablesTo(object?: {[key: string]: VariableDefinition}):function → Object: Save the variables to an object with the name specified.

>将变量保存到具有指定名称的对象。

pm.iterationData.toJSON():function → *

pm.iterationData.unset(key: string):function → void 

pm.iterationData.variables():function → Object: Return all the variables from the iterationData object.

>返回iterationData对象中的所有变量。

static pm.iterationData.isVariableScope(object: any):function → boolean:

>检查特定变量是否在范围内。

------------------------

pm.iterationData基本方法=>get(k),set(k,v),toObject()

pm.iterationData是否有toJSON()=>是

pm.iterationData变成JSON=>toJSON()

pm.iterationData是否存在clear方法=>是

pm.iterationData清除数据=>clear()

pm.iterationData是否存在unset方法=>是

pm.iterationData清除某一项数据=>unset(k)

pm.iterationData是否存在输入批量数据方法=>是

pm.iterationData输入批量数据=>addLayer(list: VariableList)

------------------------

### pm.iterationData
pm.iterationData:

The iterationData object contains data from the data file provided during a collection run.

>iterationData对象包含在集合运行期间提供的数据文件中的数据
* pm.iterationData.get(variableName:String):function → *: Returns a variable from the iteration data with the specified name.
>从具有指定名称的迭代数据中返回变量
* pm.iterationData.toObject():function → Object: Returns the iteration data as an object.
>将迭代数据作为对象返回
* pm.iterationData.addLayer(list: VariableList):function → void: Add a list of variables to iteration data.
>void：向迭代数据添加变量列表。
* pm.iterationData.clear():function → void: Clear all the data.
* pm.iterationData.has(variableName: string):function → boolean: Checks if a variable with the specified name exists in iteration data.
>检查迭代数据中是否存在具有指定名称的变量。
* pm.iterationData.set(key: string, value: any, type: string):function → void: Sets a variable, assigns it a value and type as specified.
* pm.iterationData.syncVariablesFrom(object: {[key: string]: VariableDefinition}, track?: boolean, prune?: boolean):function → Object | Undefined: Get variables from an object with the name specified.
>从具有指定名称的对象中获取变量。
* pm.iterationData.syncVariablesTo(object?: {[key: string]: VariableDefinition}):function → Object: Save the variables to an object with the name specified.
>将变量保存到具有指定名称的对象。
* pm.iterationData.toJSON():function → *: Converts the iterationData object to JSON format.
>将iterationData对象转换为JSON格式。
* pm.iterationData.unset(key: string):function → void: Un-assign the value given to a specified variable.
>取消分配给指定变量的值。
* pm.iterationData.variables():function → Object: Return all the variables from the iterationData object.
>返回iterationData对象中的所有变量。
* static pm.iterationData.isVariableScope(object: any):function → boolean: Check if a specific variable is in scope.
>检查特定变量是否在范围内。

---

---
### pm.cookies
----------------------

pm.cookies.has(cookieName:String):Function → Boolean

* Check whether a particular cookie (addressed by its name) exists for the requested domain.

pm.cookies.get(cookieName:String):Function → String

* Get the value of a particular cookie.

pm.cookies.toObject:Function → Object

* Get a copy of all cookies and their values in the form of an object. The cookies returned are the ones defined for the requested domain and path.

----------------------

----------------------

### pm.cookies
pm.cookies: [CookieList SDK Reference](https://www.postmanlabs.com/postman-collection/CookieList.html)

The cookies object contains a list of cookies that are associated with the domain to which the request was made.

pm.cookies.has(cookieName:String):Function → Boolean

* Check whether a particular cookie (addressed by its name) exists for the requested domain.

pm.cookies.get(cookieName:String):Function → String

* Get the value of a particular cookie.

pm.cookies.toObject:Function → Object

* Get a copy of all cookies and their values in the form of an object. The cookies returned are the ones defined for the requested domain and path.
### ### pm.cookies.jar
To enable programmatic access via the methods below, the cookie url must be [whitelisted](https://learning.postman.com/docs/postman/sending-api-requests/cookies/#whitelisting-domains-for-programmatic-access-of-cookies).

>若要通过以下方法启用编程访问，必须将cookie url列为白名单。

pm.cookies.jar():Function → Object

* Access the cookie jar object.

jar.set(URL:String, cookie name:String, cookie value:String, callback(error, cookie)):Function → Object

* Set a cookie using cookie name and value. One can also directly set the cookie by assinging cookie value to the cookie name within this function.

jar.set(URL:String, { name:String, value:String, httpOnly:Bool }, callback(error, cookie)):Function → Object

* Set a cookie using PostmanCookie or its compatible object.

jar.get(URL:String, token:String, callback (error, value)):Function → Object

* Gets a cookie from the cookie jar.

jar.getAll(URL:String, callback (error, cookies)):Function → Object

* Gets all the cookies from the cookie jar.

jar.unset(URL:String, token:String, callback(error)):Function → Object

* Unset a cookie.

jar.clear(URL:String, callback (error)):Function → Object

* Clear all cookies from the cookie jar.

---
### pm.test
---------------------

pm.test("信息",function () {

      运行的代码

  });

pm.test('信息', function (done) {

    setTimeout(() => {

        pm.expect(pm.response.code).to.equal(200);

        done();

    }, 1500);

  });

---------------------

pm.test的使用方法=>('信息',function(){code})

---------------------

### pm.test
pm.test(testName:String, specFunction:Function):Function

You can use this function to write test specifications inside either the Pre-request Script or Tests sandbox. Writing tests inside this function allows you to name the test accurately and this function also ensures the rest of the script is not blocked even if there are errors inside the function.

>您可以使用此函数在预请求脚本或测试沙盒中编写测试规范。在该函数中编写测试可以让您准确地命名测试，并且该函数还确保脚本的其余部分不会被阻止，即使该函数中存在错误。

The following sample test checks that everything about a response is valid to proceed.

>您可以使用以下示例测试检查有关响应的所有内容是否都可以继续。

  pm.test("response should be okay to process", function () {

      pm.response.to.not.be.error;

      pm.response.to.have.jsonBody('');

      pm.response.to.not.have.jsonBody('error');

  });

An optional done callback can be added to pm.test, to test asynchronous functions.

>您可以使用可选的done回调函数添加到pm.test中，以测试异步函数。  

pm.test('async test', function (done) {

    setTimeout(() => {

        pm.expect(pm.response.code).to.equal(200);

        done();

    }, 1500);

  });

pm.test.index():Function → Number

* Get the total number tests from a specific location.
>从特定位置获取测试总数。
### pm.expect
pm.expect(assertion:*):Function → Assertion

pm.expect is a generic assertion function. Underlying this is the [ChaiJS expect BDD library](http://chaijs.com/api/bdd/). Using this library, it is easy to write tests where the syntax becomes readable.

This function is useful to deal with assertions of data from a response or variables. For assertion test examples using pm.expect, check out [Assertion library examples](https://learning.postman.com/docs/postman/scripts/test-examples#assertion-library-examples)

>获取totapm.expect是一个通用断言函数。下面是ChaiJS expect BDD库。使用这个库，很容易编写语法可读的测试。
>此函数用于处理来自响应或变量的数据断言。对于使用pm.expect的断言测试示例，请查看断言库示例

---
### pm.response.to.have
--------------------------------------

pm.response.to.have.status(code:Number)

pm.response.to.have.status(reason:String)

pm.response.to.have.header(key:String)

pm.response.to.have.header(key:String, optionalValue:String)

pm.response.to.have.body()

pm.response.to.have.body(optionalValue:String)

pm.response.to.have.body(optionalValue:RegExp)

pm.response.to.have.jsonBody()

pm.response.to.have.jsonBody(optionalExpectEqual:Object)

pm.response.to.have.jsonBody(optionalExpectPath:String)

pm.response.to.have.jsonBody(optionalExpectPath:String, optionalValue:*)

pm.response.to.have.jsonSchema(schema:Object)

pm.response.to.have.jsonSchema(schema:Object, ajvOptions:Object)

---------------------------------------

pm.response.to.have判断状态=>status(code:Number/reason:String)

pm.response.to.have判断头信息是否有某个信息=>header(k[,v])

pm.response.to.have判断内容=>body([v:str/v:re])

pm.response.to.have判断json内容=>jsonBody([Object/k[,v]])

pm.response.to.have通过模板判断=>jsonSchema(schema:Object)

---------------------------------------

### Response Assertion API available in the test scripts
* pm.response.to.have.status(code:Number)
* pm.response.to.have.status(reason:String)
* pm.response.to.have.header(key:String)
* pm.response.to.have.header(key:String, optionalValue:String)
* pm.response.to.have.body()
* pm.response.to.have.body(optionalValue:String)
* pm.response.to.have.body(optionalValue:RegExp)
* pm.response.to.have.jsonBody()
* pm.response.to.have.jsonBody(optionalExpectEqual:Object)
* pm.response.to.have.jsonBody(optionalExpectPath:String)
* pm.response.to.have.jsonBody(optionalExpectPath:String, optionalValue:*)
* pm.response.to.have.jsonSchema(schema:Object)
* pm.response.to.have.jsonSchema(schema:Object, ajvOptions:Object)

---

---
### pm.response.to.be
--------------------------------

pm.response.to.be.info ------ 1XX

pm.response.to.be.success ------ 2XX

pm.response.to.be.redirection ------ 3XX

pm.response.to.be.clientError ------ 4XX

pm.response.to.be.serverError ------ 5XX

pm.response.to.be.error ------ 4XX OR 5XX

pm.response.to.be.ok ------ 200

pm.response.to.be.accepted ------ 202

pm.response.to.be.badRequest ------ 400

pm.response.to.be.unauthorized ------ 401

pm.response.to.be.forbidden ------ 403

pm.response.to.be.notFound ------ 404

pm.response.to.be.rateLimited ------429

--------------------------------

pm.response.to.be(success, ok, accepted) => 2XX, 200, 202

pm.response.to.be(info, redirection) => 1XX, 3XX

pm.response.to.be(2XX,200,202) => success, ok, accepted

pm.response.to.be(1XX, 3XX) => info, redirection

pm.response.to.be(clientError, badRequest, unauthorized, forbidden, notFound, rateLimited)=>4XX, 400, 401, 403, 404, 429

pm.response.to.be(serverError, error) => 5XX, 4XX OR 5XX

pm.response.to.be(4XX, 400, 401, 403, 404, 429)=>clientError, badRequest, unauthorized, forbidden, notFound, rateLimited

pm.response.to.be(5XX, 4XX OR 5XX) => serverError, error

--------------------------------

### pm.response.to.be.*
The properties inside the pm.response.to.be object allows you to easily assert a set of pre-defined rules.

pm.response.to.be.info

* Checks 1XX status code

pm.response.to.be.success

* Checks 2XX status code

pm.response.to.be.redirection

* Checks 3XX status code

pm.response.to.be.clientError

* Checks 4XX status code

pm.response.to.be.serverError

* Checks 5XX

pm.response.to.be.error

* Checks 4XX or 5XX

pm.response.to.be.ok

* Status code must be 200

pm.response.to.be.accepted

* Status code must be 202

pm.response.to.be.badRequest

* Status code must be 400

pm.response.to.be.unauthorized

* Status code must be 401

pm.response.to.be.forbidden

* Status code 403

pm.response.to.be.notFound

* Status code of response is checked to be 404

pm.response.to.be.rateLimited

* Checks whether response status code is 429

---

---
## DYnamic variables
--------------------------------

**$guid**

**$timestamp**

**$randomUUID**

**$randomAlphaNumeric**

**$randomBoolean**

**$randomInt**

**$randomColor**

**$randomHexColor**

**$randomAbbreviation**

**$randomIP**

**$randomIPV6**

**$randomMACAddress**

**$randomPassword**

**$randomLocale**

**$randomUserAgent**

**$randomProtocol**

**$randomSemver**

**$randomFirstName**

**$randomLastName**

**$randomFullName**

**$randomNamePrefix**

**$randomNameSuffix**


--------------------------------

| **Variable Name**   | **Description**   | **Examples**   | 
|:----|:----|:----|
| $guid   | uuid-v4 风格的 guid，随机性非常强   | "611c2e81-2ccb-42d8-9ddc-2d0bfa65c1b4"   | 
|     |     | "3a721b7f-7dc9-4c45-9777-516942b98e0d"   | 
|     |     | "22eca807-006b-47df-9511-e92e37f5071a"   | 
| $timestamp   | 时间戳   | 1562757107 , 1562757108 , 1562757109   | 
| $randomUUID   | 随机 36 位的 UUID   | "6929bb52-3ab2-448a-9796-d6480ecad36b"   | 
|     |     | "53151b27-034f-45a0-9f0a-d7b6075b67d0"   | 

### 随机文字、字符串、颜色（码）
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomAlphaNumeric**   | 1位随机字符或数字   | 6 , "y" , "z"   | 
| **$randomBoolean**   | 随机布尔值 (true/false)   | true , false , false , true   | 
| **$randomInt**   | 1~1000 之间的随机整数   | 802 , 494 , 200   | 
| **$randomColor**   | 随机颜色单词   | "red" , "fuchsia" , "grey"   | 
| **$randomHexColor**   | 随机颜色码   | "#47594a" , "#431e48" , "#106f21"   | 
| **$randomAbbreviation**   | 随机缩写   | SQL , PCI , JSON   | 

### 随机网络标识和 IP 地址
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomIP**   | 随机的 IPv4 地址   | 241.102.234.100 , 216.7.27.38   | 
| **$randomIPV6**   | 随机 IPv6 地址   | dbe2:7ae6:119b:c161:1560:6dda:3a9b:90a9   | 
|     |     | c482:23a4:ce4c:a668:7736:6cc5:b0b6:cc37   | 
|     |     | c791:18d1:fbba:87d8:d929:22aa:5a0a:ac3d   | 
| **$randomMACAddress**   | 随机 MAC（物理）地址   | 33:d4:68:5f:b4:c7 , 1f:6e:db:3d:ed:fa   | 
| **$randomPassword**   | 由字母和数字组成的 15 位随机密码   | t9iXe7COoDKv8k3 , QAzNFQtvR9cg2rq   | 
| **$randomLocale**   | 随机两位字母组成的语言代码 (ISO 639-1)   | "ny" , "sr" , "si"   | 
| **$randomUserAgent**   | 随机用户代理   | Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.9.8; rv:15.6) Gecko/20100101 Firefox/15.6.6   | 
|     |     | Opera/10.27 (Windows NT 5.3; U; AB Presto/2.9.177 Version/10.00)   | 
|     |     | Mozilla/5.0 (Windows NT 6.2; rv:13.5) Gecko/20100101 Firefox/13.5.6   | 
| **$randomProtocol**   | 随机协议类型   | "http" , "https"   | 
| **$randomSemver**   | 由数字组成的随机版本号   | 7.0.5 , 2.5.8 , 6.4.9   | 

### 随机姓名（英文）
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomFirstName**   | 随机的名字（英文）   | Ethan , Chandler , Megane   | 
| **$randomLastName**   | 随机姓氏（英文）   | Schaden , Schneider , Willms   | 
| **$randomFullName**   | 随机全名（名字 姓氏）   | Connie Runolfsdottir , Sylvan Fay , Jonathon Kunze   | 
| **$randomNamePrefix**   | 随机称呼   | Dr. , Ms. , Mr.   | 
| **$randomNameSuffix**   | 随机姓名后缀   | I , MD , DDS   | 

### 职业
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomJobArea**   | 随机工作范围   | Mobility , Intranet , Configuration   | 
| **$randomJobDescriptor**   | 随机职业等级   | Forward , Corporate , Senior   | 
| **$randomJobTitle**   | 随机工作标题   | International Creative Liaison ,   | 
|     |     | Product Factors Officer ,   | 
|     |     | Future Interactions Executive   | 
| **$randomJobType**   | 随机工作类型   | Supervisor , Manager , Coordinator   | 

### 随机电话号码、区域、地址
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomPhoneNumber**   | 随机 10 位数字电话号码   | 700-008-5275 , 494-261-3424 , 662-302-7817   | 
| **$randomPhoneNumberExt**   | 随机扩展号码（包含区号）   | 27-199-983-3864 , 99-841-448-2775   | 
| **$randomCity**   | 随机城市名称   | Spinkahaven , Korbinburgh , Lefflerport   | 
| **$randomStreetName**   | 随机街道名称   | Kuhic Island , General Street , Kendrick Springs   | 
| **$randomStreetAddress**   | 随机街道地址   | 5742 Harvey Streets , 47906 Wilmer Orchard   | 
| **$randomCountry**   | 随机国家名称   | Lao People's Democratic Republic , Kazakhstan , Austria   | 
| **$randomCountryCode**   | 随机两位字符的国家编码 (ISO 3166-1 alpha-2)   | CV , MD , TD   | 
| **$randomLatitude**   | 随机纬度   | 55.2099 , 27.3644 , -84.7514   | 
| **$randomLongitude**   | 随机精度   | 40.6609 , 171.7139 , -159.9757   | 

### 随机图片
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomImage**   | 随机图片地址   | [http://lorempixel.com/640/480/technics](http://lorempixel.com/640/480/technics)   | 
|     |     | [http://lorempixel.com/640/480/food](http://lorempixel.com/640/480/food)   | 
|     |     | [http://lorempixel.com/640/480/business](http://lorempixel.com/640/480/business)   | 
| **$randomAvatarImage**   | 随机头像图片   | [https://s3.amazonaws.com/uifaces/faces/twitter/johnsmithagency/128.jpg](https://s3.amazonaws.com/uifaces/faces/twitter/johnsmithagency/128.jpg)   | 
|     |     | [https://s3.amazonaws.com/uifaces/faces/twitter/xadhix/128.jpg](https://s3.amazonaws.com/uifaces/faces/twitter/xadhix/128.jpg)   | 
|     |     | [https://s3.amazonaws.com/uifaces/faces/twitter/martip07/128.jpg](https://s3.amazonaws.com/uifaces/faces/twitter/martip07/128.jpg)   | 
| **$randomImageUrl**   | 随机图片地址   | [http://lorempixel.com/640/480](http://lorempixel.com/640/480)   | 
| **$randomAbstractImage**   | 随机头像缩略图   | [http://lorempixel.com/640/480/abstract](http://lorempixel.com/640/480/abstract)   | 
| **$randomAnimalsImage**   | 随机动物图片地址   | [http://lorempixel.com/640/480/animals](http://lorempixel.com/640/480/animals)   | 
| **$randomBusinessImage**   | 随机股票业务图片   | [http://lorempixel.com/640/480/business](http://lorempixel.com/640/480/business)   | 
| **$randomCatsImage**   | 随机猫图片   | [http://lorempixel.com/640/480/cats](http://lorempixel.com/640/480/cats)   | 
| **$randomCityImage**   | 随机城市图片   | [http://lorempixel.com/640/480/city](http://lorempixel.com/640/480/city)   | 
| **$randomFoodImage**   | 随机食物图片   | [http://lorempixel.com/640/480/food](http://lorempixel.com/640/480/food)   | 
| **$randomNightlifeImage**   | 随机夜生活图片   | [http://lorempixel.com/640/480/nightlife](http://lorempixel.com/640/480/nightlife)   | 
| **$randomFashionImage**   | 随机时尚图片   | [http://lorempixel.com/640/480/fashion](http://lorempixel.com/640/480/fashion)   | 
| **$randomPeopleImage**   | 随机人物图片   | [http://lorempixel.com/640/480/people](http://lorempixel.com/640/480/people)   | 
| **$randomNatureImage**   | 随机自然风景图片   | [http://lorempixel.com/640/480/nature](http://lorempixel.com/640/480/nature)   | 
| **$randomSportsImage**   | 随机运动图片   | [http://lorempixel.com/640/480/sports](http://lorempixel.com/640/480/sports)   | 
| **$randomTechnicsImage**   | 随机科技图片   | [http://lorempixel.com/640/480/technics](http://lorempixel.com/640/480/technics)   | 
| **$randomTransportImage**   | 随机交通工具图片   | [http://lorempixel.com/640/480/transport](http://lorempixel.com/640/480/transport)   | 
| **$randomImageDataUri**   | 随机图片的 data 数据   | data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20version%3D%221.1%22%20baseProfile%3D%22full%22%20width%3D%22undefined%22%20height%3D%22undefined%22%3E%20%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20fill%3D%22grey%22%2F%3E%20%20%3Ctext%20x%3D%220%22%20y%3D%2220%22%20font-size%3D%2220%22%20text-anchor%3D%22start%22%20fill%3D%22white%22%3Eundefinedxundefined%3C%2Ftext%3E%20%3C%2Fsvg%3E   | 

### 随机金融类数据
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomBankAccount**   | 随机的8位数字银行帐号   | 09454073 , 65653440 , 75728757   | 
| **$randomBankAccountName**   | 随机的银行帐户名称(e.g. savings account, checking account)   | Home Loan Account , Checking Account , Auto Loan Account   | 
| **$randomCreditCardMask**   | 随机屏蔽的信用卡号   | 3622 , 5815 , 6257   | 
| **$randomBankAccountBic**   | 随机银行识别码 (Bank Identifier Code)   | EZIAUGJ1 , KXCUTVJ1 , DIVIPLL1   | 
| **$randomBankAccountIban**   | 随机 15-31位的国际银行帐号 (International Bank Account Number)   | MU20ZPUN3039684000618086155TKZ   | 
|     |     | BR7580569810060080800805730W2   | 
|     |     | XK241602002200395017   | 
| **$randomTransactionType**   | 随机交易类型 (e.g. invoice, payment, deposit)   | invoice , payment , deposit   | 
| **$randomCurrencyCode**   | 随机的 3 位字母的货币代码 (ISO-4217)   | CDF , ZMK , GNF   | 
| **$randomCurrencyName**   | 随机货币名称   | CFP Franc , Cordoba Oro , Pound Sterling   | 
| **$randomCurrencySymbol**   | 随机货币标志   | $ , £   | 
| **$randomBitcoin**   | 随机比特币地址   | 3VB8JGT7Y4Z63U68KGGKDXMLLH5   | 
|     |     | 1GY5TL5NEX3D1EA0TCWPLGVPQF5EAF   | 
|     |     | 14IIEXV2AKZAHSCY2KNYP213VRLD   | 

### 随机商业数据
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomCompanyName**   | 随机公司名称   | Johns - Kassulke , Grady LLC   | 
| **$randomCompanySuffix**   | 随机公司后缀(e.g. Inc, LLC, Group)   | Inc , LLC , Group   | 
| **$randomBs**   | 随机商业用语   | killer leverage schemas ,   | 
|     |     | bricks-and-clicks deploy markets ,   | 
|     |     | world-class unleash platforms   | 
| **$randomBsAdjective**   | 随机商业形容词用语   | viral , 24/7 , 24/365   | 
| **$randomBsBuzz**   | 随机商业流行词   | repurpose , harness , transition   | 
| **$randomBsNoun**   | 随机商业名词   | e-services , markets , interfaces   | 

### 随机警句（标语）
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomCatchPhrase**   | 随机名言警句   | Future-proofed heuristic open architecture ,   | 
|     |     | Quality-focused executive toolset ,   | 
|     |     | Grass-roots real-time definition   | 
| **$randomCatchPhraseAdjective**   | 随机流行语形容词   | Self-enabling , Business-focused , Down-sized   | 
| **$randomCatchPhraseDescriptor**   | 随机流行描述符号   | bandwidth-monitored , needs-based , homogeneous   | 
| **$randomCatchPhraseNoun**   | 随机生成给一个流行名词   | secured line , superstructure , installation   | 

### 随机数据库相关数据
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomDatabaseColumn**   | 随机数据库列名   | updatedAt , token , group   | 
| **$randomDatabaseType**   | 随机数据库类型   | tinyint , text   | 
| **$randomDatabaseCollation**   | 随机数据库排序规则   | cp1250_bin , utf8_general_ci , cp1250_general_ci   | 
| **$randomDatabaseEngine**   | 随机数据库引擎   | MyISAM , InnoDB , Memory   | 

### 随机日期
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomDateFuture**   | 随机未来时间   | Tue Mar 17 2020 13:11:50 GMT+0530 (India Standard Time) ,   | 
|     |     | Fri Sep 20 2019 23:51:18 GMT+0530 (India Standard Time) ,   | 
|     |     | Thu Nov 07 2019 19:20:06 GMT+0530 (India Standard Time)   | 
| **$randomDatePast**   | 随机过去时间   | Sat Mar 02 2019 09:09:26 GMT+0530 (India Standard Time) ,   | 
|     |     | Sat Feb 02 2019 00:12:17 GMT+0530 (India Standard Time) ,   | 
|     |     | Thu Jun 13 2019 03:08:43 GMT+0530 (India Standard Time)   | 
| **$randomDateRecent**   | 随机近期时间   | Tue Jul 09 2019 23:12:37 GMT+0530 (India Standard Time) ,   | 
|     |     | Wed Jul 10 2019 15:27:11 GMT+0530 (India Standard Time) ,   | 
|     |     | Wed Jul 10 2019 01:28:31 GMT+0530 (India Standard Time)   | 
| **$randomWeekday**   | 随机星期几   | Thursday , Friday , Monday   | 
| **$randomMonth**   | 随机月份   | February , May , January   | 

### 随机域名、电子邮件和用户名
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomDomainName**   | 随机完整域名   | gracie.biz , armando.biz , trevor.info   | 
| **$randomDomainSuffix**   | 随机顶级域名   | org , net , com   | 
| **$randomDomainWord**   | 随机不合法域名   | gwen , jaden , donnell   | 
| **$randomEmail**   | 随机电子邮箱地址   | Pablo62@gmail.com , Ruthe42@hotmail.com , Iva.Kovacek61@hotmail.com   | 
| **$randomExampleEmail**   | 随机电子邮箱地址，域名为example   | Talon28@example.com , Quinten_Kerluke45@example.net , Casey81@example.net   | 
| **$randomUserName**   | 随机用户名   | Jarrell.Gutkowski , Lottie.Smitham24 , Alia99   | 
| **$randomUrl**   | 随机 URL 地址   | [https://anais.net](https://anais.net) , [https://tristin.net](https://tristin.net) , [http://jakob.name](http://jakob.name)   | 

### 随机文件名和目录
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomFileName**   | 随机文件名 (包括不常用的扩展名)   | neural_sri_lanka_rupee_gloves.gdoc ,   | 
|     |     | plastic_awesome_garden.tif ,   | 
|     |     | incredible_ivory_agent.lzh   | 
| **$randomFileType**   | 随机文件类型 (包括不常用的文件类型)   | model , application , video   | 
| **$randomFileExt**   | 随机文件扩展名 (包括不常见的文件扩展名)   | war , book , fsc   | 
| **$randomCommonFileName**   | 随机文件名   | well_modulated.mpg4 ,   | 
|     |     | rustic_plastic_tuna.gif ,   | 
|     |     | checking_account_end_to_end_robust.wav   | 
| **$randomCommonFileType**   | 随机常见文件类型   | application , audio   | 
| **$randomCommonFileExt**   | 随机常见文件扩展名   | m2v , wav , png   | 
| **$randomFilePath**   | 随机文件路径   | /home/programming_chicken.cpio ,   | 
|     |     | /usr/obj/fresh_bandwidth_monitored_beauty.onetoc,   | 
|     |     | /dev/css_rustic.pm   | 
| **$randomDirectoryPath**   | 随机目录路径   | /usr/bin , /root , /usr/local/bin   | 
| **$randomMimeType**   | 随机 MIME 类型（header 中的 content-type 会用到）   | audio/vnd.vmx.cvsd ,   | 
|     |     | application/vnd.groove-identity-message ,   | 
|     |     | application/vnd.oasis.opendocument.graphics-template   | 

### 随机物料（库存、商品等）
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomPrice**   | 随机生成 100.00 ~ 999.00 之间的价格   | 531.55 , 488.76 , 511.56   | 
| **$randomProduct**   | 随机商品   | Towels , Pizza , Pants   | 
| **$randomProductAdjective**   | 随机商品形容词   | Unbranded , Incredible , Tasty   | 
| **$randomProductMaterial**   | 随机商品材料   | Steel , Plastic , Frozen   | 
| **$randomProductName**   | 随机商品名称   | Handmade Concrete Tuna , Refined Rubber Hat   | 
| **$randomDepartment**   | 随机商业分类   | Tools , Movies , Electronics   | 

### 基于英语语法的随机数据
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomNoun**   | 随机名词   | matrix , bus , bandwidth   | 
| **$randomVerb**   | 随机动词   | parse , quantify , navigate   | 
| **$randomIngverb**   | 随机带 "-ing" 的动词   | synthesizing , navigating , backing up   | 
| **$randomAdjective**   | 随机形容词   | auxiliary , multi-byte , back-end   | 
| **$randomWord**   | 随机单词   | withdrawal , infrastructures , IB   | 
| **$randomWords**   | 一些随机单词构成的字符串   | Samoa Synergistic sticky copying Grocery ,   | 
|     |     | Corporate Springs ,   | 
|     |     | Christmas Island Ghana Quality   | 
| **$randomPhrase**   | 随机短语   | You can't program the monitor without navigating the mobile XML program! ,   | 
|     |     | overriding the capacitor won't do anything, we need to compress the optical SMS transmitter! ,   | 
|     |     | I'll generate the virtual AI program, that should microchip the RAM monitor!   | 

### 随机的文本内容
| **Variable Name**   | **Decription**   | **Examples**   | 
|:----|:----|:----|
| **$randomLoremWord**   | 随机单词   | est   | 
| **$randomLoremWords**   | 随机单词构成的短语   | vel repellat nobis   | 
| **$randomLoremSentence**   | 随机单词构成的句子   | Molestias consequuntur nisi non quod.   | 
| **$randomLoremSentences**   | 随机 2~6 条句子构成的段落   | Et sint voluptas similique iure amet perspiciatis vero sequi atque. Ut porro sit et hic. Neque aspernatur vitae fugiat ut dolore et veritatis. Ab iusto ex delectus animi. Voluptates nisi iusto. Impedit quod quae voluptate qui.   | 
| **$randomLoremParagraph**   | 随机单词构成的一段话   | Ab aliquid odio iste quo voluptas voluptatem dignissimos velit. Recusandae facilis qui commodi ea magnam enim nostrum quia quis. Nihil est suscipit assumenda ut voluptatem sed. Esse ab voluptas odit qui molestiae. Rem est nesciunt est quis ipsam expedita consequuntur.   | 
| **$randomLoremParagraphs**   | 随机单词构成的 3 个段落   | Voluptatem rem magnam aliquam ab id aut quaerat. Placeat provident possimus voluptatibus dicta velit non aut quasi. Mollitia et aliquam expedita sunt dolores nam consequuntur. Nam dolorum delectus ipsam repudiandae et ipsam ut voluptatum totam. Nobis labore labore recusandae ipsam quo.   | 
|     |     | Voluptatem occaecati omnis debitis eum libero. Veniam et cum unde. Nisi facere repudiandae error aperiam expedita optio quae consequatur qui. Vel ut sit aliquid omnis. Est placeat ducimus. Libero voluptatem eius occaecati ad sint voluptatibus laborum provident iure.   | 
|     |     | Autem est sequi ut tenetur omnis enim. Fuga nisi dolor expedita. Ea dolore ut et a nostrum quae ut reprehenderit iste. Numquam optio magnam omnis architecto non. Est cumque laboriosam quibusdam eos voluptatibus velit omnis. Voluptatem officiis nulla omnis ratione excepturi.   | 
| **$randomLoremText**   | 随机单词构成的文本   | Quisquam asperiores exercitationem ut ipsum. Aut eius nesciunt. Et reiciendis aut alias eaque. Nihil amet laboriosam pariatur eligendi. Sunt ullam ut sint natus ducimus. Voluptas harum aspernatur soluta rem nam.   | 
| **$randomLoremSlug**   | 随机单词构成的 URL 部分   | eos-aperiam-accusamus , beatae-id-molestiae , qui-est-repellat   | 
| **$randomLoremLines**   | 由随机单词构成的 1~5 行数据（用回车符分隔）   | Ducimus in ut mollitia.\nA itaque non.\nHarum temporibus nihil voluptas.\nIste in sed et   | 

**补充：如果上面的例子不满足你的要求，你想从某些字符中生成一个字符串。**

```
function getRadomNum(capacity){
//chars中是你要想要的字符的数组
   var chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
   var res = "";
   for(var i = 0; i < capacity ; i ++) {
      var id = Math.ceil(Math.random()*chars.length-1);
      res += chars[id];
   }
   return res;
}
//随机的1-10位数
var name = getRadomNum( Math.ceil(Math.random()*10))
```
### 

[Edit this doc](https://github.com/postmanlabs/postman-docs/blob/develop/src/pages/docs/postman/scripts/postman-sandbox-api-reference.md)

Prerequisites

[Requests](https://learning.postman.com/docs/postman/sending-api-requests/requests/)

[Variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/)

Next Steps

[Command line integration with Newman](https://learning.postman.com/docs/postman/collection-runs/command-line-integration-with-newman/)

