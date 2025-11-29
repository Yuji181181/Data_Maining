function calc() {
    var i_num = document.getElementById('num');
    var num = parseInt(i_num.value);
    var ret;

    if (num > 200) {
        ret = "Hall";
    } else if (num > 80) {
        ret = "Lecture room";
    } else {
        ret = "Large rooms";
    }

    var res = document.getElementById('result');
    res.textContent = String(ret);
  }