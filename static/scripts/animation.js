function addLoadEvent(func){
    let oldOnLoad=window.onload;
    if(typeof oldOnLoad !="function"){
        window.onload=func;
    }else{
        window.onload=function(){
            oldOnLoad();
            func();
        }
    }
}
function addNewClass(elem,newClassName){
    if(elem.className.length==0){
        elem.className=newClassName;
    }else{
        elem.className+=(" "+newClassName);
    }
}