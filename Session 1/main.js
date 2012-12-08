
    console.log('wir');


    (function (w){
        w.cell = function() {
            var neighbors = [], state = 1;
            return {
                addNeighbors:function(arr) {
                    neighbors = arr;
                },
                getState:function() {
                    return state;
                },
                getAliveNeighbors:function(){
                    var aliveCount = 0, i=0;
                    for (;i<8;i++) {
                        if (neighbors[i].getState()) {
                            aliveCount++;
                        }
                    }
                    return aliveCount;
                },
                die: function () {
                    console.log('death');
                    state = 0;
                },
                respawn: function () {
                    console.log('alive');
                    state = 1;
                }
            }
        };


        w.game = (function () {
            var cells = [], timer = null;

            var startTimer = function () {
                timer = setInterval(newTick, 1000);
            };

            var newTick = function (){
                var i,length = cells.length;
                console.log('tick');
                for (i = 0; i< length; i++) {
                    processCell(cells[i]);
                }
            };
            var registerForTick = function(obj) {
                cells[cells.length] = obj;
            };
            var processCell = function (cell) {
                var aliveNeighbors = cell.getAliveNeighbors();
                if(cell.getState()){
                    if (aliveNeighbors < 2 || aliveNeighbors > 3) {
                        cell.die();
                    }
                }else{
                    if(aliveNeighbors === 3){
                        cell.respawn();
                    }
                }
            }
            return {
                tick: newTick,
                init: function () {
                    // add in space
                    var space = [];
                    for (var i = 0; i < 20; i++) {
                        space.push([])
                        for (var j = 0; j < 20; j++) {
                            space[i].push(new cell())
                        }
                    }
                    for (var i = 1; i < 19; i++) {
                        space.push([])
                        for (var j = 1; j < 19; j++) {
                            var neighb = [space[i-1][j-1],space[i][j-1],space[i+1][j-1],space[i-1][j],space[i+1][j],space[i-1][j+1],space[i][j+1],space[i+1][j+1]];
                            space[i][j].addNeighbors(neighb);
                        }
                    }
                    if (cells.length && timer === null) {
                        startTimer();
                    }
                }
            }
        }());

        var canvas = document.getElementById("conway");
        var ctx = canvas.getContext('2d');

    }(window));
