errors = 0;
function fail(msg) {
    console.log("fail: " + msg);
    errors = 1;
}
function pass() {
    if(!errors){
        console.log('all green');
    }
}
(function() {
    var matrice = new window.matrice();
    if (!matrice.get) {
        fail('has get');
    }
    if (matrice.get(0,0) != 0) {
        fail('get works');
    }
    if (!matrice.set) {
        fail('has set');
    }
    else {
        matrice.set(0,0);
    }
    if (matrice.get(0,0) != 1) {
        fail('set works');
    }

    if (!matrice.unset) {
        fail("has unset");
    }
    else {
        matrice.unset(0,0);
    }
    if (matrice.get(0,0)!=0) {
        fail("unset works");
    }

    matrice.set(10,10);
    if (matrice.get(10,10) != 1) {
        fail("set 10,10");
    }
    matrice.set(-5,-5);
    if (matrice.get(-5,-5) != 1) {
        fail("set -5,-5");
    }
    matrice.unset(-5,-5);
    if (matrice.get(-5,-5) != 0) {
        fail("unset -5 -5");
    }

    if (!matrice.neighbors) {
        fail("has neighbors");
    }
    if (typeof matrice.neighbors(0,1) !== "number") {
        fail("neighbors number");
    }
    if (matrice.neighbors(10,11) != 1) {
        fail("neighbors works");
    }
})();

pass();