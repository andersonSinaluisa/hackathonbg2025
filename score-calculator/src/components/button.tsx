import * as React from "react"
import { Slot } from "@radix-ui/react-slot"

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(({ className, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
        <Comp
            className={
                "inline-flex items-center justify-center whitespace-nowrap rounded-full bg-[#e6007e] px-6 py-3 text-sm font-medium text-white transition-colors hover:bg-[#c4006b] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#e6007e] focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"+
                className
            }
            ref={ref}
            {...props}
        />
    )
})
Button.displayName = "Button"

export { Button }

