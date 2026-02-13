create table if not exists streaming_event_kpis (
  window_start timestamp,
  window_end timestamp,
  event_type varchar(50),
  event_count bigint,
  total_amount numeric(18,2)
);
