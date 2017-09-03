//头部滚动
function scroll() {
    if(window.pageYOffset != null) {
        return {
            left: window.pageXOffset,
            top: window.pageYOffset
        }
    } else if(document.compatMode == "CSS1Compat")

    {
        return {
            left: document.documentElement.scrollLeft,
            top: document.documentElement.scrollTop
        }
    }
    return {
        left: document.body.scrollLeft,
        top: document.body.scrollTop
    }
}
window.onscroll = function() {
    if(scroll().top > document.querySelector(".navbar").offsetHeight) {
        document.querySelector(".navbar").classList.add("head");
        document.querySelector(".we-logo").style.marginTop = "-31px";
        document.querySelector(".go_sing_in").style.color = "#666";
        for(var i = 0; i < document.querySelectorAll(".list").length; i++) {
            document.querySelectorAll(".list")[i].style.color = "#666";
        }
    } else {
        document.querySelector(".navbar").classList.remove("head");
        document.querySelector(".go_sing_in").style.color = "#FFF";
        document.querySelector(".we-logo").style.marginTop = "0";
        for(var i = 0; i < document.querySelectorAll(".list").length; i++) {
            document.querySelectorAll(".list")[i].style.color = "#FFF";
        }
    }
}
//产品解决方案
var pSc = document.querySelectorAll(".psc");
var weColor = ["#63B7FC", "#FEA235", "#67D1B3", "#91D74C", "#FF7B91"]; // 定义color
//console.log(pSc.length);
for(var i = 0; i < pSc.length; i++) {
    pSc[i].index = i;
    pSc[i].onmouseenter = function() {
        clearInterval(timer);
        document.querySelectorAll(".info-one")[this.index].style.display = "block";
        for(var j = 0; j < pSc.length; j++) {
            pSc[j].children[0].className = "";
            pSc[j].children[1].style.color = "";
        }
        pSc[this.index].children[0].className = "animedpac-animation-holdtypes";
        pSc[this.index].children[1].style.color = weColor[this.index];
    }
    pSc[i].onmouseleave = function() {
        document.querySelectorAll(".info-one")[this.index].style.display = "none";
        pSc[this.index].children[0].className = "";
        if(this.index >= 4) {
            a = 0
        } else {
            a = this.index;
            a++;
        }
        timer = setInterval(timeBar, 800);
    }
}
var a = 0;
var timer = null;
timer = setInterval(timeBar, 800);

function timeBar() {
    for(var i = 0; i < pSc.length; i++) {
        pSc[i].children[0].className = "";
        pSc[i].children[1].style.color = "#666";
    }
    pSc[a].children[0].className = "animedpac-animation-holdtypes"
    pSc[a].children[1].style.color = weColor[a];
    a++;
    //  console.log(a);
    if(a >= 5) {
        a = 0;
    }
}

//最新动态
for(var i = 0; i < document.querySelector(".arrow_point").children.length; i++) {
    document.querySelector(".arrow_point").children[i].index = i;
    document.querySelector(".arrow_point").children[i].onclick = function() {
        //      alert(this.index);
        for(var j = 0; j < document.querySelector(".arrow_point").children.length; j++) {
            document.querySelector(".arrow_point").children[j].className = "";
        }
        document.querySelector(".arrow_point").children[this.index].className = "active";
        if(this.index == 1) {
             $(".voidlist-init").velocity({
                left: "-945px"
            }, {
                duration: 400,
                easing: "[ 250, 15 ]"
                //弹簧系数
            });
        } else {
             $(".voidlist-init").velocity({
                left: "12px"
            }, {
                duration: 400,
                easing: "[ 250, 15 ]"
                //弹簧系数
            });
        }
    }

}
document.querySelector(".r").addEventListener("click", function() {
    Velocity_time();
});
document.querySelector(".l").addEventListener("click", function() {
    Velocity_time();
});

function Velocity_time() {
    if(document.querySelector(".voidlist-init").style.left == "12px") {
        for(var j = 0; j < document.querySelector(".arrow_point").children.length; j++) {
            document.querySelector(".arrow_point").children[j].className = "";
        }
        document.querySelector(".arrow_point").children[1].className = "active";
         $(".voidlist-init").velocity({
            left: "-945px"
        }, {
            duration: 400,
            easing: "[ 250, 15 ]"
            //弹簧系数
        });
    } else {
        for(var j = 0; j < document.querySelector(".arrow_point").children.length; j++) {
            document.querySelector(".arrow_point").children[j].className = "";
        }
        document.querySelector(".arrow_point").children[0].className = "active";
        $(".voidlist-init").velocity({
            left: "12px"
        }, {
            duration: 400,
            easing: "[ 250, 15 ]"
            //弹簧系数
        });

    }
}

var aTime = 0;
var timerN = null;
timerN = setInterval(rotation, 1000);

function rotation() {
    aTime++;
    if(aTime > 5) {
        aTime = 0;
    }
    $(".right-img a").find("img").removeClass("deviation");
    $(".right-img a").find("img").eq(aTime).addClass("deviation");
     $(".big-img").velocity({
        left: -652 * aTime + "px"
    }, {
        duration: 600,
        easing: "[ 250, 15 ]"
        //弹簧系数
    });
     $(".small-img").velocity({
        left: -177 * aTime + "px"
    }, {
        duration: 600,
        easing: "[ 250, 15 ]"
        //弹簧系数
    });
}

$(".right-img a").on("click", function() {
    aTime = $(this).data("index");
    console.log($(this).data("index"));
    $(".right-img a").find("img").removeClass("deviation");
    $(this).find("img").addClass("deviation");
    $(".big-img").velocity({
        left: -652 * $(this).data("index") + "px"
    }, {
        duration: 600,
        easing: "[ 250, 15 ]"
        //弹簧系数
    });
     $(".small-img").velocity({
        left: -177 * $(this).data("index") + "px"
    }, {
        duration: 600,
        easing: "[ 250, 15 ]"
        //弹簧系数
    });
});
$(".right-img a").hover(function() {
    clearInterval(timerN);
    //  alert(1);
}, function() {
    timerN = setInterval(rotation, 1000);
})


//获取屏幕高度
console.log(window.innerHeight);
document.querySelector("#carousel-example-generic").style.height=window.innerHeight+"px";
document.querySelector(".carousel-inner").style.height=window.innerHeight+"px";
document.querySelector(".item").style.height=window.innerHeight+"px";
$(".item img").height(window.innerHeight+"px");
