const genId = (length=1)=>{
    let id = ""
    while (length > 0){
        id += Math.floor(Math.random() * 10)
        length--
    }
    return id
}

module.exports = genId