



angular.module('app', [])

//////////////////////////SETTING INITIAL LOAD//////////////////////////




//////////////////////////TEMP MODE DROPDOWN UPDATE//////////////////////////

		.controller('TEMP_Mode', function()	{
			this.display = false;
			
			this.displayGo = function()	{
				var chk = this.Mode;
				
				if (chk == 'Enabled')	{
					this.display = true;
				}	else	{
					this.display = false;
				}
			};
		});
			
		