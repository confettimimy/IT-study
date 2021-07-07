```javascript
<script>
$(document).ready(function(){

});
</script>
```

$(document).ready()는 **문서가 준비되면** 매개변수로 넣은 콜백 함수를 실행하라는 의미.

문서가 준비되면 실행되는 함수.

문서 객체가 모두 로드된 다음에 실행될 코드들을 $(document).ready(function(){}) 안에 기술해줘야 한다.

​    

**jQuery의 이벤트 메서드 중 하나**★★★

**$(document).ready() 메서드**는 굉장히 많이 사용되므로 jQuery에서는 간단하게 사용할 수 있는 형태를 제공한다.

​    

---

```javascript
$(document).ready(function(){ // Standard clickable or focusable HTML elements
   $(" a, button, select, textarea, keygen,     input ").hover(function(){ 
	  //strong, em, abbr, code, b, i, p,    iframe
	 

        //덮어씌워지는 태그는 효과줄 필요X.
	    $(this).css({ "position":"relative" });//원래의 실행객체가 이동하지 못하게 절대위치 줘버리기 
       .
       .
```

문서(최상위 객체)가 ready되면 함수 실행

표준 태그들이 hover되면 함수 실행