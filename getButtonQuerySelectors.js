require('jsdom-global')()
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
var fs=require('fs');
const scrape = require('website-scraper');
const PuppeteerPlugin = require('website-scraper-puppeteer');


const wait=ms=>new Promise(resolve => setTimeout(resolve, ms)); 
final_op=[]

function getQuerySelector(dom,elem) {

    var element = elem;
    var str = "";
  
    function loop(element) {
  
      // stop here = element has ID
      if(element.getAttribute("id")) {
        str = str.replace(/^/, " #" + element.getAttribute("id"));
        str = str.replace(/\s/, "");
        str = str.replace(/\s/g, " > ");
        return str;
      }
  
      // stop here = element is body
      if(dom.window.document.body === element) {
        str = str.replace(/^/, " body");
        str = str.replace(/\s/, "");
        str = str.replace(/\s/g, " > ");
        return str;
      }
  
      // concat all classes in "queryselector" style
      if(element.getAttribute("class")) {
        var elemClasses = ".";
        elemClasses += element.getAttribute("class");
        elemClasses = elemClasses.replace(/\s/g, ".");
        elemClasses = elemClasses.replace(/^/g, " ");
        var classNth = "";
  
        // check if element class is the unique child
        var childrens = element.parentNode.children;
  
        if(childrens.length < 2) {
          return;
        }
  
        var similarClasses = [];
  
        for(var i = 0; i < childrens.length; i++) {
          if(element.getAttribute("class") == 
  childrens[i].getAttribute("class")) {
            similarClasses.push(childrens[i]);
          }
        }
  
        if(similarClasses.length > 1) {
          for(var j = 0; j < similarClasses.length; j++) {
            if(element === similarClasses[j]) {
              j++;
              classNth = ":nth-of-type(" + j + ")";
              break;
            }
          }
        }
  
        str = str.replace(/^/, elemClasses + classNth);
  
      }
      else{
  
        // get nodeType
        var name = element.nodeName;
        name = name.toLowerCase();
        var nodeNth = "";
  
        var childrens = element.parentNode.children;
  
        if(childrens.length > 2) {
          var similarNodes = [];
  
          for(var i = 0; i < childrens.length; i++) {
            if(element.nodeName == childrens[i].nodeName) {
              similarNodes.push(childrens[i]);
            }
          }
  
          if(similarNodes.length > 1) {
            for(var j = 0; j < similarNodes.length; j++) {
              if(element === similarNodes[j]) {
                j++;
                nodeNth = ":nth-of-type(" + j + ")";
                break;
              }
            }
          }
  
        }
  
        str = str.replace(/^/, " " + name + nodeNth);
  
      }
  
      if(element.parentNode) {
        loop(element.parentNode);
      }
      else {
        str = str.replace(/\s/g, " > ");
        str = str.replace(/\s/, "");
        return str;
      }
  
    }
  
    loop(element);
  
    return str;
  
  
  }
  var cssPath = function(el) {
    var path = [];
    while (el.nodeType === Node.ELEMENT_NODE) {
        var selector = el.nodeName.toLowerCase();
        if (el.id) {
            selector += '#' + el.id;
            path.unshift(selector);
            break;
        } else {
            var sib = el, nth = 1;
            while (sib = sib.previousElementSibling) {
                if (sib.nodeName.toLowerCase() == selector)
                   nth++;
            }
            if (nth != 1)
                selector += ":nth-of-type("+nth+")";
        }
        path.unshift(selector);
        el = el.parentNode;
    }
    return path.join(" > ");
 }

function getPath(dom,x){
    list=dom.window.document.getElementsByTagName('a');
    //x="/".concat(x);
    for(let i=0;i<list.length;i++){
        
        if(list[i].href.endsWith(x)){
            //console.log('('+list[i].href+','+x+')');
            l=list[i];
            //p=getQuerySelector(dom,l);
            p=cssPath(l);
            return p;
        }
    }
}
function get_html(main_link,page_path,i){
    scrape({
        urls: [main_link.concat([page_path])],
        directory: 'NEW_FOLDER'.concat(i.toString(10)),
        plugins: [ 
        new PuppeteerPlugin({
            launchOptions: { headless: false }, /* optional */
            scrollToBottom: { timeout: 100000, viewportN: 10 } /* optional */
        })
        ]
    });
}

function main(i,page){
    temp='NEW_FOLDER';
    temp=temp.concat(i.toString(10));
    temp=temp.concat('/index.html');
    //console.log(temp)
    fs.readFile(temp, 'utf8', function(err, html){
        if (!err){
            const dom = new JSDOM(html, { includeNodeLocations: true });
            list=dom.window.document.getElementsByTagName("a");
            x=page.split("/");
            res=getPath(dom,x[x.length-1]);
            //res=dom.window.document.querySelector(res);
            final_op[i]=res;
            //console.log(i);
            //console.log(res);
        }
        else{
            console.log("error");
        }
      })
}

function getStates(main_link,b_loop)
{
    for(let i=1;i<b_loop.length;i++)
    {
        main(i-1,b_loop[i])
    }
}

let rawdata = fs.readFileSync('output.json');
let list_links = JSON.parse(rawdata);
main_link=list_links['Main']
b_loop=list_links['Loop']

//main_link='http://localhost/lab-website/hp';
//b_loop=['/hp.html','/hp_projects.html','/hp_videos.html','/hp_students.html','/hp.html']
for(let i=0;i<b_loop.length-1;i++)
{
    get_html(main_link,b_loop[i],i)
}
//get_html(main_link,b_loop[0],1);
//wait(10*1000).then(() => main(1,b_loop[0]));    
wait(20*1000).then(() => getStates(main_link,b_loop));
wait(40*1000).then(() => console.log(final_op));
wait(1*1000).then(() => console.log(main_link.concat(b_loop[0])));
