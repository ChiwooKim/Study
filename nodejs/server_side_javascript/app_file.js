const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
app.locals.pretty = true
app.use(bodyParser.urlencoded({ extended: false}));
app.set('views', './views_file');
app.set('view engine', 'pug');

app.get('/topic/new', function(req, res){
  res.render('new');
})

app.get('/topic', function(req, res){
  fs.readdir('data', function(err, files){
    if (err) {
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    res.render('view', {topics:files});
  })
});

app.get('/topic/:id', function(req, res){
  const id = req.params.id;
  fs.readdir('data', function(err, files){
    if (err) {
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    fs.readFile('data/'+id, 'utf8', function(err, data){
      if (err) {
        console.log(err);
        res.status(500).send('Internal Server Error');
      }
      res.render('view', {title:id, topics:files, description:data});  
    })
  })
})

app.post('/topic', function(req, res){
  let title = req.body.title;
  let description = req.body.description;
  fs.writeFile('data/'+title, description, function(err){
    if (err) {
      res.status(500).send('Internal Server Error');
    }
    res.send('Success!');
  });
})

app.listen(3000, function(){
  console.log('Connected, 3000port');
})