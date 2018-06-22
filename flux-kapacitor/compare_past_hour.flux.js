current = from(db:"telegraf")
        |> filter(fn:(r) => r._measurement == "cpu" and r._field == "usage_user")
        |> range(start:-1h)

past = from(db:"telegraf")
        |> filter(fn:(r) => r._measurement == "cpu" and r._field == "usage_user")
        |> range(start:-2h, stop:-1h)
        |> shift(shift:1h)

difference = join(tables:{current:current, past:past}, 
                  on:["host","cpu"], 
                  fn: (tables) => tables.current["_value"] - tables.past["_value"])
        |> limit(n:10)
