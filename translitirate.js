let dictionary = new Map();
let rus_letters = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р',
					'с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
						'А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р',
						'С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я', ' '];
let eng_translet =	['a','b','v','g','d','e','e','j','z','i','i','k','l','m','n','o','p','r',
					 's','t','u','f','h','c','ch','sh','sc','','y','','e','iu','ia',
						'A','B','V','G','D','E','E','J','Z','I','I','K','L','M','N','O','P','R',
						'S','T','U','F','H','C','CH','SH','SC','','Y','','E','IU','IA', ' '];
rus_letters.forEach(function(item, i, arr){
dictionary.set(item, eng_translet[i]);
});
	

input.oninput = function() {
	
	let input_word;
	let output_word = [];	
	
	result.value = ' ';
	input_word = input.value
	for(let i = 0; i < input_word.length; i++){
		output_word[i] = dictionary.get(input_word[i])
	}
	

	result.value = output_word.join('');
	
};