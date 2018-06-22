var current = batch
      |query('SELECT usage_user FROM "telegraf"."autogen"."cpu"')
          .period(1h)
          .every(1m)
          .groupBy('sensor_id')
      |last('usage_user')
          .as('current_usage')

var past = batch
      |query('SELECT usage_user FROM "telegraf"."autogen"."cpu"')
          .period(1h)
          .offset(1h)
          .every(1m)
          .groupBy('host', 'cpu')
      |shift(1h)
      |last('usage_user')
          .as('past_usage')

var joined_data = current
      |join(past)
          .as('current', 'past')
          .fill(0.0)
          .tolerance(1m)

var performance_error = joined_data
      |eval(lambda: "current.current_usage" - "past.past_usage")
        .as('difference')
