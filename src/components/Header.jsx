import React from 'react'
import { HiOutlineSearch } from "react-icons/hi";

export default function Header() {
  return (
    <div className='bg-white h-16 px-4 flex justify-between items-center border-b border-gray-200'>
        <div className='relative'>
            <HiOutlineSearch fontsize={20} className='absolute top-1/2 -translate-y-1/2 left-3 text-gray-400'/>
            <input 
                type="text" 
                placeholder='Search...' 
                className="text-sm focus:outline-none active:outline-none h-10  w-[24rem] border border-gray-300 round-sm px-4 pl-10"></input>
        </div>
        <div>side buttons</div>
    </div>
  )
}
