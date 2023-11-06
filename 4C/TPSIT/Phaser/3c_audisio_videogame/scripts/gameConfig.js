window.addEventListener('load', () => {
    let config = {
        type: Phaser.AUTO,
        width: 400,
        height: 320,
        backgroundColor: 0x220283,
        physics: {
            default: 'arcade',
            arcade: {
                // debug: true,
                gravity: {
                    y: 0
                }
            }
        },
        scale: {
            mode: Phaser.Scale.FIT,
            autoCenter: Phaser.Scale.CENTER_BOTH,
            parent: "thegame"
        },
        pixelArt: true,
        scene: [GameScene, UIScene, LoseScene]
    }
    const game = new Phaser.Game(config)
    })  

    class TitleScene extends Phaser.Scene {
        constructor() {
            super('titleScene')
        }
        preload() {
        }
        create() {
        }
        update() {
        }
    }

    class WinScene extends Phaser.Scene {
        constructor() {
            super('winScene')
        }
        preload() {
        }
        create() {
        }
        update() {
        }
    }
    
    class LoseScene extends Phaser.Scene {
        constructor() {
            super('loseScene')
        }
        init(data){
            this.remainingHealth = data.health
            console.log(this.remainingHealth);
            console.log('help');
        }
    
        //PRELOAD

        preload() {
            this.cameras.main.setBackgroundColor(0xcc0000)
    
        }
    
        //CREATE

        create() {
            this.add.text(100,100,'GAME OVER!')
        }
    
        //UPDATE

        update() {
        }
    }