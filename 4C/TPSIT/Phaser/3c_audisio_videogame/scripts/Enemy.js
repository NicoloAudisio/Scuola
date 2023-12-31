class Enemy extends Entity{
    constructor(scene, x, y, textureKey, damage, type, speed){
        super(scene,x,y,textureKey,'Enemy',type)
        const anims = scene.anims
        const animFrameRate = 4
        this.textureKey = textureKey
        this.damage = damage
        this.type = type
        this.speed = speed
        anims.create({
            key: this.type+'enemy-left',
            frames: anims.generateFrameNames(this.textureKey, {
                prefix: this.type+'-walk-left-',
                suffix: '.png',
                start: 1,
                end: 3,
                zeroPad: 2
            }),
            frameRate: animFrameRate,
            repeat: -1
        })
        anims.create({
            key: this.type+'enemy-right',
            frames: anims.generateFrameNames(this.textureKey, {
                prefix: this.type+'-walk-right-',
                suffix: '.png',
                start: 1,
                end: 3,
                zeroPad: 2
            }),
            frameRate: animFrameRate,
            repeat: -1
        })
        anims.create({
            key: this.type+'enemy-up',
            frames: anims.generateFrameNames(this.textureKey, {
                prefix: this.type+'-walk-up-',
                suffix: '.png',
                start: 1,
                end: 3,
                zeroPad: 2
            }),
            frameRate: animFrameRate,
            repeat: -1
        })
        anims.create({
            key: this.type+'enemy-down',
            frames: anims.generateFrameNames(this.textureKey, {
                prefix: this.type+'-walk-down-',
                suffix: '.png',
                start: 1,
                end: 3,
                zeroPad: 2
            }),
            frameRate: animFrameRate,
            repeat: -1
        })
        let dir = Math.floor(Math.random()*4)
        switch (dir) {
            case 0:
                this.body.setVelocity(0,-this.speed)//su
                this.anims.play(this.type+'enemy-up')
                break
            case 1:
                this.body.setVelocity(-this.speed,0)//sinistra
                this.anims.play(this.type+'enemy-left')
                break
            case 2:
                this.body.setVelocity(0,this.speed)//giù
                this.anims.play(this.type+'enemy-down')
                break
            case 3:
                this.body.setVelocity(this.speed,0)//destra
                this.anims.play(this.type+'enemy-right')
                break
            default:
                break;
        }    }

    update(){
        const {speed} = this
        const enemyBlocked = this.body.blocked

        if (enemyBlocked.down || enemyBlocked.up || enemyBlocked.left || enemyBlocked.right){
            let possibleDirections = []
            for (const direction in enemyBlocked){
                possibleDirections.push(direction)
            }
            const newDirection = possibleDirections[Math.floor(Math.random()*4)+1]
            switch (newDirection) {
                case 'up':
                    this.body.setVelocity(0,-this.speed)//su
                    this.anims.play(this.type+'enemy-up')
                    break
                case 'left':
                    this.body.setVelocity(-this.speed,0)//sinistra
                    this.anims.play(this.type+'enemy-left')
                    break
                case 'down':
                    this.body.setVelocity(0,this.speed)//giù
                    this.anims.play(this.type+'enemy-down')
                    break
                case 'right':
                    this.body.setVelocity(this.speed,0)//destra
                    this.anims.play(this.type+'enemy-right')
                    break
                case 'none':
                    this.body.setVelocity(0,0)//niente
                    this.anims.stop()
                    break
                default:
                    break;
            }
        }
    }
}