typedef enum setState {
  start = 0,
  open_set,
  close_set,
  open_double,
  close_double,
  error
} setState;

void cgc_parse_set(char * right) {
  setState state = start;
  while (*right && state != close_set) {
    if (*right == '|') {
      switch(state) {
        case start:
          state = open_set;
        case open_double:
          break;
        default:
          state = close_set;
          break;
      }
    } else if (*right == '"') {
      switch(state) {
        case open_double:
          state = close_double;
          break;
        case close_double:
          state = error;
          goto end;
          break;
        default:
          state = open_double;
          break
        }
    } else {
      switch(state) {
        case close_double:
          state = error;
          goto end;
        default:
          break;
        }
    }
    right++;
  }
end:
  if ( state == error ) {
    //error handling
  }
  return; 
}