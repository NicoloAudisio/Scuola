class UIScene extends Phaser.Scene {
    constructor(){
        super({key: 'UIScene', active: true})
    }

    //CREATE

    create(){
        //console.log('ui scene');
        this.coinScore = 0
        this.coinText = this.add.text(300,4,'Punti: '+this.coinScore, {font: '10px', fill:'#ffffff'})
        this.healthbar = new Healthbar(this, 8, 2, 100)
    }

    //UPDATE

    updateCoins(){
        this.coinScore+= 1
        this.coinText.setText('Punti: '+this.coinScore)
    }

    //RESET

    reset(){
        this.coinScore = 0
        this.coinText.setText('Punti: '+this.coinScore)
        this.healthbar.updateHealth(100)
    }
}