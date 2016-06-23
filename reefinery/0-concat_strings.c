/*concat str*/
char *concat_strings(char *dest, const char *src)
{
  int i, j;
  i = 0;
  j = 0;
  
  while(dest[i]!= '\0')
    {
      i++;
    }
  /* i = i +1;*/
  while(src[j]!= '\0')
    {
      dest[i] = src[j];
      j++;
      i++;
    }
  return dest;
}
