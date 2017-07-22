//var Hello = React.createClass({
//  render: function() {
//    return <div>Hello {this.props.name}</div>;
//  }
//});

//ReactDOM.render(
//  <Hello name="World" />,
//  document.getElementById('suggest_list')
//);


/* var start = new Date().getTime();
var ExampleApplication = React.createClass({
  render: function(){
      var current = new Date().getTime();
      return <p>Time elapsed: {current-start}</p>;
  }
});

var update = setInterval(function(){
  ReactDOM.render(
    <ExampleApplication/>,
    document.getElementById('suggest_list')
  )
}, 500);*/

var ExampleApplication = React.createClass({
  render: function(){
    var listItems = this.props.data.suggestions.map(function(item){
      return(
        <li key={item.id}>{item.suggestion}</li>
      )
    });
    return <ul>{listItems}</ul>
  }
});

var ExampleApplicationFactory =
    React.createFactory(ExampleApplication);

var update = setInterval(function(){
  $.ajax({
    url: "/suggestions",
    success: function(data){
      ReactDOM.render(
        ExampleApplicationFactory({data: data}),
        document.getElementById('suggest_list')
      );
    }
  })
}, 500);
