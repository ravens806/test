const tabs = document.querySelectorAll(".tabs li a");
const btn = document.querySelectorAll(".btn li a");

for(let i = 0;i < tabs.length;i++){
    tabs[i].addEventListener("click",function(e) {
        e.preventDefault();
        for(let j = 0;j < tabs.length;j++){
            tabs[j].classList.remove("active");
        }
        for(let j = 0;j < tabs.length;j++){
            btn[j].classList.remove("active");
        }
        tabs[i].classList.add("active");
        btn[i].classList.add("active");
    });
};
