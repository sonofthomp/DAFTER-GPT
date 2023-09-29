let completion = "";

let modifyPageTo = function(val, iteration) {
  val.replace('=\n', ' ');
  let injected_code = `
  console.log(document.getElementsByClassName('gmail_signature')[0].parentElement.children[0].outerHTML);
  document.getElementsByClassName('gmail_signature')[0].parentElement.children[0].outerHTML = \`<pre>` + val + `</pre>\`;
  `;
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.executeScript(tabs[0].id, { code: injected_code });
  });
}

document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('clickIt');

    checkPageButton.addEventListener('click', function() {
      chrome.tabs.getSelected(null, function(tab) {
        let phrase = document.getElementById("prompt-input").value;
        let model = document.getElementById("model").value;
        let length = document.getElementById("length").value;
        modifyPageTo('Generating result...');

        // Temporary ngrok link because I don't want to permanently host the Python API
        // If you're trying to run this yourself, replace this URL with whichever one you use
        fetch('https://3a8f-2a09-bac1-76c0-1358-00-289-41.ngrok-free.app/?phrase='+phrase+'&model='+model+'&length='+length)
          .then(resp => resp.json())
          .then(json => json['response'])
          .then(val => modifyPageTo(val, '1'));
      });
    }, false);
  }, false);

// document.addEventListener('DOMContentLoaded', function() {
//   var addButton = document.getElementById('addButton');

//   addButton.addEventListener('click', function() {
//     chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//       chrome.tabs.executeScript(tabs[0].id, { code: "document.body.innerHTML += '<p>New paragraph added!</p>';" });
//     });
//   })
// });