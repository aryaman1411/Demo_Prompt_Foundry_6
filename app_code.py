Here is a basic starter code for a web-based e-commerce application using Node.js and Express.js. This code includes basic functionality such as product listing and user authentication.

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const passport = require('passport');
const AzureStore = require('connect-azuretables')(session);

// Initialize the Express app
const app = express();

// Set up middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(session({
    secret: 'your-secret-key',
    store: new AzureStore({
        table: 'sessions',
        accessKey: 'your-access-key',
        storageAccount: 'your-storage-account'
    }),
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());

// Define routes
app.get('/', (req, res) => {
    res.send('Welcome to our e-commerce platform!');
});

app.get('/products', (req, res) => {
    // Fetch products from Azure SQL Database and send as response
});

app.post('/login', passport.authenticate('local', {
    successRedirect: '/products',
    failureRedirect: '/'
}));

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server is running on port ${port}`));
```

This is a very basic setup and you would need to add more functionality according to your requirements. You can deploy this code to GitHub by initializing a new repository and pushing the code.

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin master
```

Remember to replace 'your-secret-key', 'your-access-key', and 'your-storage-account' with your actual Azure credentials. Also, you need to implement the product fetching logic in the '/products' route and add a local strategy for Passport.js in the '/login' route.