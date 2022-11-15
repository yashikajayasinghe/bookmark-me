
```pip install -r requirements.txt```

https://dotnetthoughts.net/developing-and-deploying-azure-functions-with-codespaces/

```wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4```

Once installed, you can run func --version command in the terminal - which should display 3.x. Now you can debug the function using F5 key or you can click on the debug button and click on the debug button. Now Codespaces will run your application in http://localhost:7071/api/HttpTrigger1 and which is forwarded to a global unique address where you can browse and test the azure function. As I mentioned earlier in Codespaces you will get all the development / debugging experience with VS Code.

https://microsoft.github.io/AzureTipsAndTricks/blog/tip364.html

```npm i -g azure-functions-core-tools@4 --unsafe-perm true```


https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-project-for-codespaces?langId=py