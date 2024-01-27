package models

import "time"

type User struct {
	Id        int       `json:"id"`
	Name      string    `json:"name"`
	Email     string    `json:"email"`
	Password  string    `json:"password"`
	CreatedAt time.Time `json:"created_at"`
	UpdateAt  time.Time `json:"update_at"`
}

type Measurements struct {
	Id         int       `json:"id"`
	UserId     int       `json:"user_id"`
	Weight     float64   `json:"weight"`
	Height     float64   `json:"height"`
	Bodyfat    float64   `json:"body_fat"`
	Created_at time.Time `json:"created_at"`
}
