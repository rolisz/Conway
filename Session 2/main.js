(function(w){
    w.matrice = function() {
        this.rows = {};
    };
    matrice.prototype.get = function(row,column) {
        if(this.rows[row] === undefined){
           return 0;
        }
        if ( this.rows[row][column] === undefined ){
            return 0;
        }
        return this.rows[row][column];
    };
    matrice.prototype.set = function(row,column) {
        if (this.rows[row] === undefined) {
            this.rows[row] = {}
        }
        this.rows[row][column] = 1;

    };
    matrice.prototype.unset = function(row,column) {
        delete this.rows[row][column];
    };
    matrice.prototype.neighbors = function(row,column) {
        var i, j,count = 0;
        for (i = row-1; i<=row+1; i++) {
            for (j = column-1; j<= column+1;j++) {
                count+=this.get(i,j);
            }
        }
        return count;
    }


    w.game = function () {
        this.livingCells = [];
        this.timer = null;
    };
    game.prototype.startTimer = function (){
        timer = setInterval(this.tick, 1000);
    };
    game.prototype.tick = function() {
        var deadNeighbors = [], i, length = this.livingCells.length;
        for (i=0; i< lenght; i++) {
            var row = this.livingCells[i].row,column = this.livingCells[i].col;
            if (matrice.get(row,column)) {
                var nrN = matrice.neighbors(row,column);
                if ( nrN < 2 || nrN > 3) {
                    matrice.unset(row,column);
                }
            }
        }
    }
}(window));