const router = require("express").Router()


router.get("/", (req, res)=>{res.render("login")})
router.get("/register", (req, res)=>{res.render("register")})
router.get("/index", (req, res)=>{res.render("dashboard")
})

module.exports = router
