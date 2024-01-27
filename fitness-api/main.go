package main

import (
	"fitness-api/cmd/handlers"
	"fitness-api/cmd/storage"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()
	e.GET("/", handlers.Home)
	storage.InitDB()

	e.Use(middleware.Logger(), middleware.Recover())

	e.POST("/users", handlers.CreateUser)
	e.POST("/measurements", handlers.CreateMeasurement)
	e.PUT("/users/:id", handlers.HandleUpdateUsers)
	e.PUT("measurements/:id", handlers.HandleUpdateMeasurements)

	e.Logger.Fatal(e.Start(":8080"))
}
