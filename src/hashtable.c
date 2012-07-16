#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "mu/hashtable.h"

#ifdef __cplusplus
extern "C" {
#endif

DLL_VARIABLE int _cmp_string(const void* key1, size_t len1, const void* key2, size_t len2)
{
	if(len1 == len2)
		return memcmp(key1, key2, len1);
	else if(len1 > len2)
		return 1;
	else 
		return -1;
}

DLL_VARIABLE size_t _hash_string(const char *vkey, size_t len)
{
	size_t hash = 5381;
	size_t i;
	const char *key = (char *) vkey;

	for (i = 0; i < len; i++)
		hash = ((hash << 5) + hash) + key[i]; /* hash * 33 + char */

	return hash;
}

#ifdef __cplusplus
}
#endif

