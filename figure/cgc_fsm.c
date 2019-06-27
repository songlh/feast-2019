 typedef enum setState {
     start = 0,
     open_set,
     close_set,
     open_double,
     close_double,
     error
 } setState;

 bool cgc_parse_set(char * right) {
     setState state = start;

     while (*right && state != close_set) {
         if (*right == '|') {
             switch(state) {
                 case start:
                     state = open_set;
                     break;
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
                 case open_set:
                     state = open_double;
                     break;
                 default:
                     state = error;
                     goto end;
             }
         } else {
             switch(state) {
                 case open_double:
                     break;
                 default:
                     state = error;
                     goto end;
             }
         }
         right++;
     }
 end:
     if ( state != close_set ) {
         return false;
     }
     return true; 
 }